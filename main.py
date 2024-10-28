from src.data_utils import read_company_names
from src.image_search import search_ddg_images
from src.image_utils import download_images

if __name__ == "__main__":
    company_file = '/Users/motta/company-logo-scraper/companies.txt'
    company_list = read_company_names(company_file)
    
    if company_list:
        max_results = 5
        all_urls = []
        print(f"Companies found: {company_list}")
        
        for company in company_list:
            print(f"Searching for images for {company}...")
            image_urls = search_ddg_images(company, max_results)  # Call the search function
            all_urls.append({company: image_urls})  # Store company name and its corresponding URLs in a dictionary format
            
        # Print all collected URLs to verify
        print("\nCollected Image URLs:")
        for company_info in all_urls:
            for company, urls in company_info.items():
                print(f"{company}: {urls}")
                
                
        # Step 3: Download images
        download_images(all_urls)

    else:
        print("No companies found or error reading file.")