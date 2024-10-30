import argparse
from concurrent.futures import ThreadPoolExecutor
from src.data_utils import read_company_names
from src.image_search import search_ddg_images
from src.image_utils import download_images

def main():
    parser = argparse.ArgumentParser(description='Company Logo Scraper')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to the text file containing company names. This argument is required.')
    parser.add_argument('-n', '--num-results', type=int, required=True, help='Number of logo results to search for each company. This argument is required.')
    parser.add_argument('-p', '--process-image', action='store_true', help='Flag to enable image processing (background removal and cropping). Default is enabled.')

    args = parser.parse_args()
    
    company_file = args.file
    company_list = read_company_names(company_file)
    
    if not company_file:
        print("No companies found or error reading file.")
        return
    
    max_results = args.num_results
    all_urls = []
    
    print(f"Companies found: {company_list}")
    for company in company_list:
        print(f"Searching for images for {company}...")
        image_urls = search_ddg_images(company, max_results)
        all_urls.append({company: image_urls})
        
    print("\nCollected Image URLs:")
    for company_info in all_urls:
        for company, urls in company_info.items():
            print(f"{company}: {urls}")
            
    with ThreadPoolExecutor() as executor:
        futures = []
        for company_info in all_urls:
            for company, urls in company_info.items():
                for index, url in enumerate(urls):
                    futures.append(executor.submit(download_images, company, url, index, args.process_image))
                    
        for future in futures:
            future.result()


if __name__ == "__main__":
    main()