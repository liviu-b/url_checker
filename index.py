import requests

def is_secure_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad HTTP status codes 
        return response.url.startswith('https://')  # Check if the URL starts with 'https://'

    except requests.exceptions.RequestException:
        return False  # Unable to connect or other issues, consider it not secure

if __name__ == "__main__":
    website_url = input("Enter the website URL:")

    if is_secure_website(website_url):
        print(f"{website_url} is a secure website.")
    else:
        print(f"{website_url} is not a secure website.")