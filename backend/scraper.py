import requests
from bs4 import BeautifulSoup

def fetch_documentation(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 403:
        raise Exception("Access Forbidden: Check headers or permissions.")
    soup = BeautifulSoup(response.text, 'html.parser')
    sections = []
    for section in soup.find_all(['h1', 'h2', 'h3', 'p']):
        sections.append(section.get_text())
    return sections


# URLs for documentation
DOC_URLS = {
    "segment": "https://segment.com/docs/?ref=nav",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_all_docs():
    all_docs = {}
    for key, url in DOC_URLS.items():
        all_docs[key] = fetch_documentation(url)
    return all_docs
