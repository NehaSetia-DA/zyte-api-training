"""
Exercise: Network Capture - Nike Product API
Showcases Zyte API's network capture feature for Nike's infinite scroll product API.
"""

import sys
from pathlib import Path
import json
from base64 import b64decode
import requests
from typing import Dict, List, Optional
import time
import os

# Add parent directory to path to import utils
sys.path.append(str(Path(__file__).parent.parent))
from utils.config import ZYTE_API_KEY, ZYTE_API_ENDPOINT

def capture_nike_network_requests(url: str, filter_pattern: str, max_retries: int = 3) -> Optional[List[Dict]]:
    """
    Capture and analyze Nike product API network requests during page scroll.
    Args:
        url (str): Nike product listing page
        filter_pattern (str): Pattern to filter Nike API requests
        max_retries (int): Retry attempts
    Returns:
        list: Processed network captures
    """
    payload = {
        "url": url,
        "browserHtml": True,
        "actions": [
            {"action": "scrollBottom"},
        ],
        "networkCapture": [
            {
                "filterType": "url",
                "httpResponseBody": True,
                "value": filter_pattern,
                "matchType": "contains"
            }
        ]
    }
    for attempt in range(max_retries):
        try:
            print(f"Capturing Nike network requests (attempt {attempt + 1}/{max_retries})...")
            response = requests.post(
                ZYTE_API_ENDPOINT,
                auth=(ZYTE_API_KEY, ""),
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            captures = result.get("networkCapture", [])
            if not captures:
                print("No network captures found. Retrying...")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
                    continue
                return None
            print(f"{captures=}")
            result = process_nike_captures(captures)
            print(f"{result=}")
            return result
        except requests.exceptions.RequestException as e:
            print(f"Request error: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return None
        except Exception as e:
            print(f"Error: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2 ** attempt)
                continue
            return None
    return None

def process_nike_captures(captures: List[Dict]) -> List[Dict]:
    """
    Process Nike network captures and extract product data.
    """
    processed_data = []
    for capture in captures:
        try:
            print(f"\n[DEBUG] Capture URL: {capture.get('url')}, Status: {capture.get('status')}, Method: {capture.get('method')}")
            body = capture.get("httpResponseBody", "")
            if not body:
                print(capture)
                continue
            decoded_text = b64decode(body).decode()
            data = json.loads(decoded_text)
            print(f"{data=}")
            for grouping in data.get("productGroupings", []):
                for product in grouping.get("products", []):
                    product_data = {
                        "name": product.get("copy", {}).get("title", ""),
                        "subtitle": product.get("copy", {}).get("subTitle", ""),
                        "price": product.get("prices", {}).get("currentPrice", ""),
                        "image_url": product.get("colorwayImages", {}).get("portraitURL", ""),
                        "product_url": product.get("pdpUrl", {}).get("url", ""),
                        "url": capture.get("url"),
                        "method": capture.get("method"),
                        "status": capture.get("status"),
                        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
                    }
                    processed_data.append(product_data)
        except Exception as e:
            print(f"Error processing capture: {str(e)}")
            continue
    return processed_data

def save_to_json(data: List[Dict], filename: str = "nike_network_captures.json"):
    """
    Save captured data to a JSON file in the responses directory.
    """
    if not data:
        return
    os.makedirs("responses", exist_ok=True)
    if not filename.startswith("responses/"):
        filename = os.path.join("responses", filename)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump({
            'captures': data,
            'metadata': {
                'count': len(data),
                'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
            }
        }, f, indent=2, ensure_ascii=False)

def main():
    url = "https://www.nike.com/in/w/running-37v7j"
    filter_pattern = "/discover/product_wall/v1/marketplace/IN/language/en-GB/consumerChannelId/d9a5bc42-4b9c-4976-858a-f159cf99c647"
    print(f"Analyzing network requests for: {url}")
    captures = capture_nike_network_requests(url, filter_pattern)
    if captures:
        print(f"\nFound {len(captures)} Nike product API captures")
        filename = f"nike_network_capture_{time.strftime('%Y%m%d_%H%M%S')}.json"
        save_to_json(captures, filename)
        print(f"Saved results to {filename}")
        print("\nSample Captured Products:")
        print("-" * 50)
        for product in captures[:2]:
            print(f"\nName: {product['name']}")
            print(f"Price: {product['price']}")
            print(f"Product URL: {product['product_url']}")
            print(f"API URL: {product['url']}")
            print(f"Status: {product['status']}")
            print("-" * 30)
    else:
        print("No Nike product API captures found or error occurred")

if __name__ == "__main__":
    main()