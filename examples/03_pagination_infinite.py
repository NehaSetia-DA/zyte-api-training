"""
Example 3: Infinite Scroll - Quote Scraper
Demonstrates infinite scroll handling using Zyte API.
Link to Documentation: https://docs.zyte.com/zyte-api/usage/reference.html#operation/extract/request/actions
"""

import sys
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import json
import time
from typing import List, Dict, Optional
import os

# Add parent directory to path to import utils
sys.path.append(str(Path(__file__).parent.parent))
from utils.config import ZYTE_API_KEY, ZYTE_API_ENDPOINT

def scrape_infinite_scroll(url: str, max_scrolls: int = 3) -> List[Dict]:
    """
    Scrape data from an infinite scroll page.
    
    Args:
        url (str): Target URL
        max_scrolls (int): Maximum number of scroll operations
        
    Returns:
        list: Collection of quotes from all scrolls
    """
    payload = {
        "url": url,
        "browserHtml": True,
        "javascript": True,
        "actions": [
            {
                "action": "scrollBottom",
                # "maxScrollCount": max_scrolls,
                "onError": "continue"
            },
        ]
    }
    
    try:
        response = requests.post(
            ZYTE_API_ENDPOINT,
            auth=(ZYTE_API_KEY, ""),
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        result = response.json()
        
        if result and "browserHtml" in result:
            soup = BeautifulSoup(result["browserHtml"], 'html.parser')
            quotes = []
            
            for quote_div in soup.select('.quote'):
                try:
                    text = quote_div.select_one('.text').get_text(strip=True)
                    author = quote_div.select_one('.author').get_text(strip=True)
                    tags = [tag.get_text(strip=True) for tag in quote_div.select('.tags .tag')]
                    
                    quotes.append({
                        'text': text[1:-1],  # Remove surrounding quotes
                        'author': author,
                        'tags': tags,
                        'scraped_at': time.strftime("%Y-%m-%d %H:%M:%S")
                    })
                except Exception as e:
                    print(f"Error extracting quote: {str(e)}")
                    continue
            
            return quotes
        else:
            print("No valid response received from Zyte API.")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def save_to_json(quotes: List[Dict], filename: str = None):
    """
    Save quotes to a JSON file in the responses directory.
    """
    if not quotes:
        return
    os.makedirs("responses", exist_ok=True)
    if not filename:
        filename = f"quotes_infinite_scroll_{time.strftime('%Y%m%d_%H%M%S')}.json"
    if not filename.startswith("responses/"):
        filename = os.path.join("responses", filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({
            'quotes': quotes,
            'metadata': {
                'count': len(quotes),
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }, f, indent=2, ensure_ascii=False)

def main():
    # Example usage
    url = "http://quotes.toscrape.com/scroll"
    print(f"Starting infinite scroll scrape for: {url}")
    
    quotes = scrape_infinite_scroll(url, max_scrolls=20)
    
    if quotes:
        print(f"\nFound {len(quotes)} total quotes")
        
        # Save to JSON
        filename = f"quotes_infinite_scroll_{time.strftime('%Y%m%d_%H%M%S')}.json"
        save_to_json(quotes, filename)
        print(f"Saved results to {filename}")
        
        # Print sample quotes
        print("\nSample Quotes:")
        print("-" * 50)
        for quote in quotes[:2]:  # Show first 2 quotes
            print(f"\nText: {quote['text']}")
            print(f"Author: {quote['author']}")
            print(f"Tags: {', '.join(quote['tags'])}")
            print("-" * 30)
    else:
        print("No quotes found or error occurred")

if __name__ == "__main__":
    main() 