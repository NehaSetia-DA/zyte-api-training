"""
Exercise 2: Infinite Scroll - Nike Product Scraper
Demonstrates infinite scroll handling using Zyte API for Nike's website.
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

def extract_products_with_infinite_scroll(url: str, max_scrolls: int = 3) -> Optional[List[Dict]]:
    """
    Extract products from a page with infinite scrolling.
    
    Args:
        url (str): Target URL
        max_scrolls (int): Maximum number of scroll operations
        
    Returns:
        list: Collection of products from all scrolls
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
            }
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
            products = []
            
            # Nike product selectors
            for product in soup.select('[data-testid="product-card"]'):
                try:
                    name = product.select_one('[data-testid="product-card__title"]')
                    price = product.select_one('[data-testid="product-price"]')
                    image = product.select_one('img')
                    
                    if name and price and image:
                        data = {
                            "name": name.get_text(strip=True),
                            "price": price.get_text(strip=True),
                            "image_url": image.get('src', ''),
                            "product_url": product.select_one('a').get('href', '') if product.select_one('a') else ''
                        }
                        products.append(data)
                except Exception as e:
                    print(f"Error extracting product: {str(e)}")
                    continue
            
            return products
        else:
            print("No valid response received from Zyte API.")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def save_to_json(products: List[Dict], filename: str = None):
    """
    Save products to a JSON file in the responses directory.
    """
    if not products:
        return
    os.makedirs("responses", exist_ok=True)
    if not filename:
        filename = f"nike_products_infinite_scroll_{time.strftime('%Y%m%d_%H%M%S')}.json"
    if not filename.startswith("responses/"):
        filename = os.path.join("responses", filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({
            'products': products,
            'metadata': {
                'count': len(products),
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }, f, indent=2, ensure_ascii=False)

def main():
    # Example usage with Nike's website - Men's Running section
    url = "https://www.nike.com/in/w/mens-running-shoes-37v7jznik1zy7ok"
    print(f"Starting infinite scroll scrape for: {url}")
    
    products = extract_products_with_infinite_scroll(url, max_scrolls=3)
    
    if products:
        print(f"\nFound {len(products)} total products")
        
        # Save to JSON
        filename = f"nike_products_infinite_scroll_{time.strftime('%Y%m%d_%H%M%S')}.json"
        save_to_json(products, filename)
        print(f"Saved results to {filename}")
        
        # Print sample products
        print("\nSample Products:")
        print("-" * 50)
        for product in products[:2]:  # Show first 2 products
            print(f"\nName: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Image URL: {product['image_url']}")
            print(f"Product URL: {product['product_url']}")
            print("-" * 30)
    else:
        print("No products found or error occurred")

if __name__ == "__main__":
    main()