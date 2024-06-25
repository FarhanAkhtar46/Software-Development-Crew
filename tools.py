import json
import os
import requests
from langchain.tools import tool

class BrowserTools:
    @tool("Scrape and summarize website")
    def scrape_and_summarize_website(url):
        """Scrape the given website and summarize its content."""
        # Placeholder for scraping and summarizing logic
        return f"Summary of the website {url}"

class SearchTools:
    def __init__(self):
        self.api_key = os.getenv('API_KEY')
        self.api_url = 'https://api.openai.com/v1/engines/text-davinci-002/jobs'

    @tool("Search internet")
    def search_internet(query):
        """Useful to search the internet about a given topic and return relevant results."""
        return SearchTools.search(query)

    @tool("Search instagram")
    def search_instagram(query):
        """Useful to search for Instagram posts about a given topic and return relevant results."""
        query = f"site:instagram.com {query}"
        return SearchTools.search(query)

    def search(query, n_results=5):
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query})
        headers = {
            'X-API-KEY': os.getenv('SERPER_API_KEY'),
            'content-type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        results = response.json()['organic']
        stirng = []
        for result in results[:n_results]:
            try:
                stirng.append('\n'.join([
                    f"Title: {result['title']}",
                    f"Link: {result['link']}",
                    f"Snippet: {result['snippet']}",
                    "\n-----------------"
                ]))
            except KeyError:
                next

        content = '\n'.join(stirng)
        return f"\nSearch result: {content}\n"
