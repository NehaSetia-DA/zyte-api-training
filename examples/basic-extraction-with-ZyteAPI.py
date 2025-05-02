import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ZYTE_API_KEY = os.getenv('ZYTE_API_KEY')
ZYTE_API_ENDPOINT = "https://api.zyte.com/v1/extract"

def basic_scraper(url):
    response = requests.post(
        ZYTE_API_ENDPOINT,
        auth=(ZYTE_API_KEY, ""),
        json= {
            "url": url,
            "browserHtml": True,
            #"httpResponseBody": True
            #"product": True,
            "productList": True,
            #"article": True,
            #"articleList": True,
            "actions": [
                {
                    "action": "scrollBottom",
                    
                }
             ]
        }
    )
    return response.json()

if __name__ == "__main__":
    url = "https://www.nike.com/in/w/running-37v7j"
    result = basic_scraper(url)
    print(result)



# example url: https://www.nike.com/in/w/mens-running-shoes-37v7jznik1zy7ok
# example url: https://www.nike.com/in/w/running-37v7j



# 1. **browserHtml**: This setting, when enabled (set to true), retrieves the browser-rendered HTML of a page. It can be used when you need the fully rendered HTML of a page, especially when the page content is dependent on JavaScript. It's important to note that this field is not compatible with httpResponseBody in the same request.
# 2. **httpResponseBody**: This field, when set to true, retrieves the raw HTTP response body. It should be used when you need the original HTML as returned by the server without any client-side rendering by JavaScript. This cannot be used in conjunction with browserHtml.
# 3. **productList**: This field is useful for extracting product list data from pages that contain multiple products, such as product category pages. When enabled, it captures a list of products, which is efficient for minimizing the number of requests needed to extract basic product information.
# 4. **article and articleList**: These fields are similar to productList but are instead used for pages that contain articles. Use article for a single article page and articleList for pages containing multiple articles, like a news site with multiple posts.
# 5. **actions**: Actions in the Zyte API allow you to perform additional operations such as waiting for certain elements to load or scrolling down a page. These actions are executed during the scraping session, and the data is extracted after actions are completed or timed out. This is particularly useful for interacting with dynamic or heavily JavaScript-dependent pages.
# When using these features, consider the target page's structure and what kind of data you need to extract, as some fields are mutually exclusive and choosing between browserHtml or httpResponseBody could depend on whether you need fully rendered or raw HTML.