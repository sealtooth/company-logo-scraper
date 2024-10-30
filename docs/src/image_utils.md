Module src.image_utils
======================

Functions
---------

`crop_image_tightly(image_path)`
:   Crops an image tightly around non-empty areas.
    
    Args:
        image_path (str or BytesIO): Path or BytesIO object of the image to be cropped.
    
    Returns:
        Image: A tightly cropped version of the image, or the original image if no cropping is possible.
    
    This function detects non-empty areas in an image to tightly crop it. It works by 
    either using the alpha channel (for images with transparency) or by converting the 
    image to grayscale and finding the non-white bounding box for images without transparency.

`download_images(company, url, index, process)`
:   Downloads a single image from the given URL and optionally processes it.
    
    Args:
        company (str): The name of the company.
        url (str): The URL from which the image will be downloaded.
        index (int): The index of the image (used for naming).
        process (bool): If True, the image will be processed (e.g., tightly cropped).
    
    The function downloads the image for a given company from the specified URL.
    If the `process` argument is True, the function will crop the image tightly 
    around non-empty areas before saving it locally in the `downloaded_logos` folder.