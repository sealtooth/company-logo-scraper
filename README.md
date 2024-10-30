# Company Logo Scraper

A Python script that automatically searches for company logos using DuckDuckGo, downloads them, and optionally processes the images (e.g., cropping and background removal). This tool is useful for quickly gathering company logos, especially for presentation slides, marketing materials, or other projects.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Documentation](#documentation)
- [Contributing](#contributing)

## Installation
To use this project locally, clone the repository and install the dependencies:

```sh
# Clone the repository
git clone https://github.com/yourusername/company-logo-scraper.git
cd company-logo-scraper

# Create a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

## Usage
To search for and download company logos, run:

```sh
python main.py -f companies.txt -n 5 -p -v
```

- `-f`, `--file`: Path to the text file containing company names. This argument is required.
- `-n`, `--num-results`: Number of logo results to search for each company. This argument is required.
- `-p`, `--process-image`: Enable image processing (cropping and background removal). Default is enabled.
- `-v`, `--verbose`: Enable verbose mode for detailed output (optional).

Example:
```sh
python main.py -f companies.txt -n 3 -p
```

The above command will search for three logos for each company listed in `companies.txt`, process the images, and save them locally.

## Features
- **Automated Logo Search**: Automatically searches DuckDuckGo for company logos using the given company names.
- **Image Processing**: Crops and removes the background from the logos (optional feature).
- **Multithreading**: Downloads images concurrently to improve performance.

## Documentation
The project documentation is available in the `docs/` directory, which includes detailed information about each module:

- [Data Utils Documentation](docs/src/data_utils.md): Handles reading company names from a text file.
- [Image Search Documentation](docs/src/image_search.md): Manages searching DuckDuckGo for images.
- [Image Utils Documentation](docs/src/image_utils.md): Functions for downloading and processing images.

For more in-depth technical details, refer to these module-level docs.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

