"""
Exercise 1: Network Capture - Nike API Direct Access
Capture and analyze product data directly from Nike's API endpoints.
"""

import sys
from pathlib import Path
import json
import requests
from typing import List, Dict, Optional
import time

# Add parent directory to path to import utils
sys.path.append(str(Path(__file__).parent.parent))
from utils.config import ZYTE_API_KEY

def get_nike_products(category: str) -> List[Dict]:
    """
    TODO: Implement this function to:
    1. Configure the Nike API URL for the given category
    2. Set up proper headers for the API request
    3. Use Zyte proxy to make the request
    4. Process and extract product information
    
    Args:
        category (str): Product category (e.g., 'mens-shoes', 'football', 'basketball')
        
    Returns:
        list: Processed products data
    """
    # TODO: Configure the Nike API URL based on category
    base_url = "https://api.nike.com/discover/product_wall/v1/marketplace/IN/language/en-GB"
    consumer_id = "d9a5bc42-4b9c-4976-858a-f159cf99c647"
    
    # TODO: Set up the API URL with proper parameters
    api_url = f"{base_url}/consumerChannelId/{consumer_id}"
    
    # TODO: Configure headers
    headers = {
        "nike-api-caller-id": "nike:dotcom:browse:wall.client:2.0",
        "Referer": "https://www.nike.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    }
    
    # TODO: Set up Zyte proxy configuration
    proxies = {
        "http": f"http://{ZYTE_API_KEY}:@api.zyte.com:8011",
        "https": f"http://{ZYTE_API_KEY}:@api.zyte.com:8011"
    }
    
    try:
        # TODO: Make the API request via Zyte proxy
        # TODO: Process the response and extract products
        # TODO: Format the product data
        pass
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def format_product(product_data: Dict) -> Dict:
    """
    TODO: Implement this function to format raw product data
    
    Args:
        product_data (dict): Raw product data from API
        
    Returns:
        dict: Formatted product information
    """
    # TODO: Extract and format product details
    # - Title
    # - Subtitle
    # - Price and currency
    # - Image URL
    # - Product URL
    pass

def save_to_json(products: List[Dict], filename: str = "nike_products.json"):
    """
    Save products to a JSON file in the responses directory.
    
    Args:
        products (list): List of product dictionaries
        filename (str): Output filename
    """
    if not products:
        return
        
    # Create responses directory if it doesn't exist
    Path("responses").mkdir(exist_ok=True)
    
    # Save file in responses directory
    filepath = Path("responses") / filename
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump({
            'products': products,
            'metadata': {
                'count': len(products),
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }, f, indent=2, ensure_ascii=False)

def main():
    # Example categories
    categories = {
        'football': 'football-1gdj0',
        'basketball': 'basketball-3glsm',
        'running': 'running-37v7j'
    }
    
    for category_name, category_id in categories.items():
        print(f"\nProcessing {category_name} category...")
        products = get_nike_products(category_id)
        
        if products:
            print(f"\nFound {len(products)} products:")
            print("-" * 50)
            
            # Show first 3 products as sample
            for product in products[:3]:
                print(f"\n🛒 {product.get('title')} - {product.get('subtitle')}")
                print(f"💰 Price: {product.get('price')} {product.get('currency')}")
                print(f"🔗 URL: {product.get('product_url')}")
                print("-" * 30)
            
            # Save to JSON
            filename = f"nike_{category_name}_{time.strftime('%Y%m%d_%H%M%S')}.json"
            save_to_json(products, filename)
        else:
            print(f"No products found for {category_name}")

if __name__ == "__main__":
    main()

"""
Exercise Tasks:
1. Complete the implementation of get_nike_products()
2. Implement format_product() to process the API response
3. Add error handling for API requests
4. Extract key product information (name, price, images, URLs)
5. Handle rate limiting and retries

Bonus:
- Extract additional product metadata
- Implement pagination to get more products
- Add filtering options by product attributes
- Handle multiple product variants
""" 