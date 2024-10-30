def read_company_names(file_path):
    """
    Reads company names from a given text file and returns them as a list.

    Args:
        file_path (str): The path to the .txt file containing company names, one per line.

    Returns:
        list: A list of company names read from the specified file. 
              Returns an empty list if the file does not exist.

    This function reads company names line by line from a text file, allowing the user
    to specify their own list of companies to search for logos.
    """
    try:
        with open (file_path, 'r') as file:
            company_names = file.read().splitlines()
        return company_names
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []