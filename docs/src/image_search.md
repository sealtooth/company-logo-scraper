Module src.image_search
=======================

Functions
---------

`search_ddg_images(query, max_results)`
:   Searches DuckDuckGo for images related to the given query and returns a list of image URLs.
    
    Args:
        query (str): The search query (e.g., company name) to look for.
        max_results (int): The maximum number of image URLs to return.
    
    Returns:
        list: A list of URLs for the found images, filtered from DuckDuckGo search results.
    
    This function uses DuckDuckGo Search to find image URLs related to the provided search query.
    Only the URLs of the images are extracted and returned as a list.