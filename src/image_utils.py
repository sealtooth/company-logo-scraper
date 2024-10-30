import os
import requests
from PIL import Image
from io import BytesIO

def download_images(company, url, index, process):
    """Downloads a single image and optionally processes it."""
    try:
        response = requests.get(url)
        response.raise_for_status()
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