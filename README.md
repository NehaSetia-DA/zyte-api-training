# Zyte API Training Workshop

A comprehensive workshop for learning web scraping using Zyte API and Cursor IDE. This repository contains examples, exercises, and solutions for various web scraping scenarios.

## 🎯 Workshop Overview

Learn to build robust web scrapers using Zyte API, handling different scraping scenarios:
- Network traffic capture and API analysis
- Classic pagination handling
- Infinite scroll management
- Form submission and interaction
- Error handling and best practices

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- [Zyte API account](https://www.zyte.com/zyte-api/?utm_campaign=DIS-ONBOARD&utm_activity=Community&utm_medium=social&utm_source=Discord&utm_content=zyte_api_Web32) and API key
- Basic understanding of Python and web scraping concepts

### Installation

1. Clone the repository:
```bash
git clone https://github.com/NehaSetia-DA/zyte-api-training
cd zyte-api-training
```

2. Create and activate virtual environment:
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
```bash
# Create .env file
cp .env.example .env

# Add your Zyte API key to .env
echo "ZYTE_API_KEY=your-api-key-here" > .env
```

5. Verify setup:
```bash
python check_setup.py
```

## 📁 Repository Structure

### Examples
Ready-to-use example implementations:
- `01_network_capture.py` - Network traffic capture and analysis
- `02_pagination_classic.py` - Classic pagination handling
- `03_pagination_infinite.py` - Infinite scroll implementation
- `04_form_submission.py` - Form handling and submission
- `basic-extraction.py` - Basic data extraction

### Exercises
Practice exercises with increasing complexity:
- `01_network_capture.py` - Nike product data extraction
- `02_pagination_classic.py` - Job listings scraper
- `03_infinite_scroll.py` - Nike Product Extraction using Infinite scroll actions Zyte API. 
- `04_form_submission.py` - Quote search form automation
- `practice_scenarios.py` - Additional challenges

### Solutions
Complete implementations of exercises with best practices:
- Error handling
- Rate limiting
- Data validation
- Optimal performance

### Utils
Helper functions and configurations:
- API configuration
- Common utilities
- Shared functions

## 🎓 Workshop Content

### 1. Network Capture (Nike Case Study)
- Capturing API endpoints
- Analyzing network traffic
- Extracting product data
- Handling pagination

### 2. Classic Pagination (Indeed.com)
- Page-by-page navigation
- Data extraction
- Error handling
- Rate limiting

### 3. Infinite Scroll (Nike Search)
- Dynamic content loading
- Scroll management
- Duplicate detection
- Performance optimization

### 4. Form Submission (Quotes to Scrape)
- Form interaction
- Multi-step processes
- Response validation
- Error recovery

## 💡 Best Practices

1. **Rate Limiting**
   - Implement delays between requests
   - Use exponential backoff
   - Handle API limits

2. **Error Handling**
   - Try-except blocks
   - Retry mechanisms
   - Logging and monitoring

3. **Data Management**
   - Proper storage formats
   - Data validation
   - Duplicate handling

4. **Code Organization**
   - Modular structure
   - Clear documentation
   - Reusable components

## 🛠️ Tools Used

- [Zyte API](https://www.zyte.com/zyte-api/?utm_campaign=DIS-ONBOARD&utm_activity=Community&utm_medium=social&utm_source=Discord&utm_content=zyte_api_edc) - All in one Web Scraping API.
- [Cursor IDE](https://www.cursor.com/downloads) - AI-powered development environment

## 📚 Additional Resources

### Zyte API Documentation
- [Getting Started Guide](https://docs.zyte.com/zyte-api/usage/index.html) - Complete overview and usage guide
- [API Usage Examples](https://docs.zyte.com/zyte-api/usage/index.html#zapi-usage) - Common usage patterns and examples
- [HTTP Mode](https://docs.zyte.com/zyte-api/usage/http.html) - HTTP request handling
- [Browser Automation Mode](https://docs.zyte.com/zyte-api/usage/browser.html) - Browser automation features
- [Browser Actions](https://docs.zyte.com/zyte-api/usage/browser.html#zapi-actions) - Available browser interactions
- [Extraction API](https://docs.zyte.com/zyte-api/usage/extract/index.html) - Data extraction capabilities
- [Proxy Mode](https://docs.zyte.com/zyte-api/usage/proxy-mode.html) - Proxy configuration and usage


## 🤝 Contributing

Feel free to:
- Report issues
- Suggest improvements
- Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


