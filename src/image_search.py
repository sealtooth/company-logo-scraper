from duckduckgo_search import DDGS

def search_ddg_images(query, max_results):
    """
    Searches DuckDuckGo for images related to the given query and returns a list of image URLs.

    Args:
        query (str): The search query (e.g., company name) to look for.
        max_results (int): The maximum number of image URLs to return.

    Returns:
        list: A list of URLs for the found images, filtered from DuckDuckGo search results.

    This function uses DuckDuckGo Search to find image URLs related to the provided search query.
    Only the URLs of the images are extracted and returned as a list.
    """
    # Initialize DDG search session    
    with DDGS() as ddgs:
        results = ddgs.images(keywords=query + " logo", max_results=max_results)
        image_urls = []
        # Extract URLs from search results if 'image' key exists
        for result in results:
            if 'image' in result:
                image_urls.append(result['image'])

        return image_urls