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


        # app.py

from flask import Flask, render_template, request
from url_checker.checker import check_url  # Adjust the import based on your actual module

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                result = check_url(url)  # Replace with your actual function
            except Exception as e:
                error = str(e)
        else:
            error = "Please enter a URL."
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
