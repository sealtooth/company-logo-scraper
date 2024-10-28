import requests
from PIL import Image
from io import BytesIO
import os

def download_images(company_urls):
    """
    Downloads images from a list of URLs for each company and saves them locally.

    Args:
        company_urls (list): A list of dictionaries where each dictionary contains a company name and its associated image URLs.
    """
    
    # Create the folder 'downloaded_logos' in the parent directory of src/
    base_directory = os.path.join(os.path.dirname(__file__), '..')
    download_directory = os.path.join(base_directory, 'downloaded_logos')
    os.makedirs(download_directory, exist_ok=True)

    
    for company_info in company_urls:
        for company, urls in company_info.items():
            print(f"Downloading images for {company}...")
            # Create sub-folder for each company
            company_folder = os.path.join(download_directory, company)
            os.makedirs(company_folder, exist_ok=True)
            
            for index, url in enumerate(urls):
                try:
                    response = requests.get(url)
                    response.raise_for_status()
                    img = Image.open(BytesIO(response.content))
                    
                    # Crop the image tightly around the logo
                    img_cropped = crop_image_tightly(BytesIO(response.content))
                    
                    # Save the cropped image with a meaningful namae
                    image_filename = f'{company_folder}/{company}_logo_{index + 1}.png'
                    img_cropped.save(image_filename, 'PNG')
                    print(f"Saved image {image_filename}")
                
                except requests.exceptions.RequestException as e:
                    print(f"Failed to download {url}: {e}")
                except IOError as e:
                    print(f"Failed to save image for {url}: {e}")
                    


def crop_image_tightly(image_path):
    """
    Crops an image tightly around the non-empty areas.

    Args:
        image_path (str): Path to the image file to be cropped.

    Returns:
        Image object: A tightly cropped version of the image.
    """
    try:
        img = Image.open(image_path)

        # If the image has an alpha channel (transparency)
        if img.mode in ('RGBA', 'LA'):
            # Split the image into separate channels
            alpha = img.getchannel('A')
            bbox = alpha.getbbox()
            if bbox:
                img_cropped = img.crop(bbox)
                return img_cropped
        else:
            # Convert the image to grayscale and create a mask to find the non-white regions
            gray = img.convert('L')
            # Create a mask by thresholding (keep anything darker than a certain value)
            mask = gray.point(lambda x: 0 if x > 245 else 255)
            bbox = mask.getbbox()
            if bbox:
                img_cropped = img.crop(bbox)
                return img_cropped

    except IOError as e:
        print(f"Error in cropping image {image_path}: {e}")
        return None

    return img  # If nothing is cropped, return the original image