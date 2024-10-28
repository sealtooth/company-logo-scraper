from duckduckgo_search import DDGS

def search_ddg_images(query, max_results):
    """
    Searches DuckDuckGo for images related to the query and returns a list of image URLs.

    Args:
        query (str): The search query (e.g., company name).
        max_results (int): Maximum number of image URLs to return.

    Returns:
        list: A list of URLs for the found images.
    """
    
    with DDGS() as ddgs:
        results = ddgs.images(keywords=query + " logo", max_results=max_results)
        
        image_urls = []
        for result in results:
            if 'image' in result:
                image_urls.append(result['image'])

        return image_urls