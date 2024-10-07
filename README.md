# URL Checker

A simple Python script to check if a website URL is secure by verifying if it uses HTTPS. This project uses the `requests` library to send an HTTP request to the provided URL and checks the response.

## Features

- Check if a website uses HTTPS
- Handle exceptions for non-responsive websites or bad URLs
- Simple command-line interface for URL input

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/url-checker.git

2. Navigate to the project directory:

   ```bash
   cd url-checker

3. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate

4. Install the required packages:

   ```bash
   pip install -r requirements.txt


## Usage
To run the script, use the following command in your terminal:

1. To run the script, use the following command in your terminal:

   ```bash
   python index.py

2. You will be prompted to enter a website URL:

   ```bash
   Enter the website URL: https://example.com

3. The script will then check if the website is secure (uses HTTPS) and display a message:

   ```bash
   https://example.com is a secure website.


## LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.