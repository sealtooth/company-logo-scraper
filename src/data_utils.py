def read_company_names(file_path):
    """ Reads company names from a .txt file and returns a list of company names. """
    try:
        with open (file_path, 'r') as file:
            company_names = file.read().splitlines()
        return company_names
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []