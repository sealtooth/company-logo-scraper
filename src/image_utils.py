import os
import requests
from PIL import Image
from io import BytesIO

def download_images(company, url, index, process):
    """
    Downloads a single image from the given URL and optionally processes it.

    Args:
        company (str): The name of the company.
        url (str): The URL from which the image will be downloaded.
        index (int): The index of the image (used for naming).
        process (bool): If True, the image will be processed (e.g., tightly cropped).

    The function downloads the image for a given company from the specified URL.
    If the `process` argument is True, the function will crop the image tightly 
    around non-empty areas before saving it locally in the `downloaded_logos` folder.
    """
    try:
        # Download the image from the given URL
        response = requests.get(url)
        response.raise_for_status()
        
        # Validate the Content-Type to ensure it is an image
        content_type = response.headers.get('Content-Type')
        if content_type not in ['image/png', 'image/jpeg', 'image/jpg']:
            print(f"Skipped URL {url} - Content-Type {content_type} is not a valid image type.")
            return
        
        img = Image.open(BytesIO(response.content))

        # Optionally process the image (crop, remove background)
        if process:
            img = crop_image_tightly(BytesIO(response.content))

        # Save the image
        company_folder = os.path.join('downloaded_logos', company)
        os.makedirs(company_folder, exist_ok=True)
        image_filename = f'{company}_logo_{index + 1}.png'
        image_path = os.path.join(company_folder, image_filename)
        img.save(image_path, 'PNG')
        print(f"Saved image {image_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
    except IOError as e:
        print(f"Failed to save image for {url}: {e}")              

def crop_image_tightly(image_path):
    """
    Crops an image tightly around non-empty areas.

    Args:
        image_path (str or BytesIO): Path or BytesIO object of the image to be cropped.

    Returns:
        Image: A tightly cropped version of the image, or the original image if no cropping is possible.

    This function detects non-empty areas in an image to tightly crop it. It works by 
    either using the alpha channel (for images with transparency) or by converting the 
    image to grayscale and finding the non-white bounding box for images without transparency.
    """
    try:
        img = Image.open(image_path)

        # If the image has an alpha channel, use it to determine non-empty areas
        if img.mode in ('RGBA', 'LA'):
            # Split the image into separate channels
            alpha = img.getchannel('A')
            bbox = alpha.getbbox()
            if bbox:
                img_cropped = img.crop(bbox)
                return img_cropped
        else:
            # Convert to grayscale to find non-white areas
            gray = img.convert('L')
            # Create a binary mask: anything lighter than a threshold is considered background
            mask = gray.point(lambda x: 0 if x > 245 else 255)
            bbox = mask.getbbox()
            if bbox:
                img_cropped = img.crop(bbox)
                return img_cropped

    except IOError as e:
        print(f"Error in cropping image {image_path}: {e}")
        return None

    # If no suitable bounding box found, return the original image
    return img