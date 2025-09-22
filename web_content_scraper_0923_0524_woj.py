# 代码生成时间: 2025-09-23 05:24:52
import requests
import numpy as np
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

"""
A simple Python script to scrape web content using requests and BeautifulSoup.

This script is designed to retrieve web content from a given URL, parse it, and provide
basic functionality to navigate through the links found on the page.

Attributes:
    None

Methods:
    scrape_web_content(url): Scrapes the content of the given URL and returns the content.
    get_links(content): Extracts all links from the given HTML content.
    follow_links(base_url, links): Follows the links and retrieves their content.

Example:
    >>> content = scrape_web_content('https://example.com')
    >>> links = get_links(content)
    >>> followed_content = follow_links('https://example.com', links)

Note:
    This script assumes that the webpage is accessible and the links are valid.
    Error handling is included to manage potential issues.
"""


def scrape_web_content(url):
    """Scrapes the content of the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def get_links(content):
    """Extracts all links from the given HTML content."""
    try:
        soup = BeautifulSoup(content, 'html.parser')
        links = [urljoin(soup.new_string(), tag.get('href')) for tag in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        print(f"Error parsing content: {e}")
        return []


def follow_links(base_url, links):
    """Follows the links and retrieves their content."""
    try:
        results = {}
        for link in links:
            if urlparse(link).netloc == urlparse(base_url).netloc:  # Only follow links within the same domain
                results[link] = scrape_web_content(link)
            else:
                results[link] = None
        return results
    except Exception as e:
        print(f"Error following links: {e}")
        return {}

# Example usage
if __name__ == '__main__':
    url = 'https://example.com'
    content = scrape_web_content(url)
    if content:
        links = get_links(content)
        followed_content = follow_links(url, links)
        print(followed_content)
    else:
        print(f"Failed to retrieve content from {url}")
