import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://example.com"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all links
for link in soup.find_all("a"):
    print(link.get("href"))
