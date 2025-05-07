# Zyte API & Cursor Workshop (1-Hour Plan)

## Workshop Overview
Duration: 1 hour
Target Audience: Developers new to Cursor and Zyte API
Prerequisites: Basic Python knowledge, Cursor IDE installed

## Detailed Timeline

### 1. Workshop Setup & Introduction (5 mins)
- [ ] Welcome participants
- [ ] Quick introduction to workshop objectives
- [ ] Verify prerequisites:
  - Cursor IDE installed: [link](https://www.cursor.com/downloads)
  - Python 3.8+ installed
  - Zyte API account created: [link](https://www.zyte.com/zyte-api/?utm_campaign=DIS-ONBOARD&utm_activity=Community&utm_medium=social&utm_source=Discord&utm_content=zyte_api_Web32) 
- Workshop GitHub Repository: [link](https://github.com/NehaSetia-DA/zyte-api-training)
- [ ] Share workshop materials:
  - GitHub repository link
  - Documentation links
  - Sample code templates

### 2. Cursor IDE Familiarization (10 mins)
- [ ] Quick interface tour:
  - File explorer
  - Terminal integration
  - AI assistant features
- [ ] Basic operations demo:
  - Creating new files
  - Running Python scripts
  - Using the terminal
- [ ] Hands-on exercise (5 mins):
  ```python
  # Create a simple test.py file
  print("Hello, Cursor!")
  ```
  - Create file
  - Run script
  - Verify output

### 3. Zyte API Introduction (10 mins)
- [ ] Overview of Zyte API capabilities
- [ ] Key features demonstration:
  - Intelligent Proxy Rotation
  - BrowserHTML 
  - Handling Captchas 
  - Automatic Data Extraction
  - Managing Bans 
- [ ] API documentation walkthrough
- [ ] Keep Zyte API key handy

### 4. Project Setup (10 mins)

#### Step 1: Directory Contents Explanation

1. **examples/** - Ready-to-use example scripts
   - `01_network_capture.py` - Network traffic capture implementation
   - `02_pagination_classic.py` - Classic pagination handling
   - `03_pagination_infinite.py` - Infinite scroll implementation
   - `04_form_submission.py` - Form handling example
   - `basic-extraction.py` - Basic data extraction example

2. **exercises/** - Practice exercises
   - `01_network_capture.py` - Network capture exercise
   - `02_pagination_classic.py` - Pagination exercise
   - `03_infinite_scroll.py` - Infinite scroll exercise
   - `04_form_submission.py` - Form submission exercise
   - `practice_scenario.py` - Additional practice scenario

3. **responses/** - Storage directory for scraped data
   - Organized by date and exercise
   - Contains JSON output files
   - Stores scraped product data
   - Maintains execution logs
   - Preserves raw API responses

4. **solutions/** - Complete solution implementations
   - Contains working code for all exercises
   - Includes best practices and error handling
   - Demonstrates optimal implementation
   - Features detailed comments and documentation
   - Serves as reference for exercise completion

5. **Key Files**
   - `check_setup.py` - Verifies environment setup
   - `requirements.txt` - Project dependencies
   - `.env` - Environment variables and API key
   - `README.md` - Project documentation
   - `workshop_plan.md` - Detailed workshop guide
   - `system_architecture.md` - Comprehensive system diagrams and architecture documentation
   - `test_examples.py` - Test cases for example implementations


#### Step 2: Set Up Python Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Verify activation
which python  # or 'where python' on Windows
```

#### Step 3: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt

# Verify installations
pip list
```

#### Step 4: Configure Environment
```bash
# Create .env file (if not exists)
touch .env

# Add your Zyte API key to .env
echo "ZYTE_API_KEY=your-api-key-here" > .env
```

#### Step 5: Verify Setup
```bash
# Run the setup verification script
python check_setup.py
```



#### Getting Started Steps

1. **Initial Setup**:
   - Clone the repository
   - Create and activate virtual environment
   - Install dependencies
   - Configure .env with API key

2. **Verify Setup**:
   - Run check_setup.py
   - Ensure all dependencies are installed
   - Verify API key configuration

3. **Start Learning**:
   - Begin with basic-extraction.py example
   - Progress through numbered examples
   - Complete exercises in order

4. **Common Issues**:
   - Virtual environment not activated
   - Missing .env file or API key
   - Incorrect dependencies
   - Permission issues

### 5. Basic Scraping Example (15 mins)
- [ ] Simple website scraping demo
- [ ] Basic extraction code:
  ```python
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
          json={
              "url": url,
              "browserHtml": True
          }
      )
      return response.json()
  ```
- [ ] Hands-on exercise:
  - Create scraper
  - Extract basic data
  - Save results

### 6. Advanced Features Overview (10 mins)
- [ ] Quick overview of advanced features:
  - Pagination handling
  - Infinite scroll
  - Form submission
  - Error handling
- [ ] Code snippets for each feature
- [ ] Q&A session

## Workshop Materials

### Pre-workshop Checklist
- [ ] Cursor IDE installed
- [ ] Python 3.8+ installed
- [ ] Zyte API account created
- [ ] API key ready
- [ ] Workshop materials downloaded

### Code Templates
1. Environment Configuration:
```bash
# .env
ZYTE_API_KEY=your-api-key
```

2. Basic Configuration:
```python
# utils/config.py
import os
from dotenv import load_dotenv

load_dotenv()
ZYTE_API_KEY = os.getenv('ZYTE_API_KEY')
ZYTE_API_ENDPOINT = "https://api.zyte.com/v1/extract"
```

3. Basic Scraper:
```python
# solutions/01_basic_scraper.py
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
ZYTE_API_KEY = os.getenv('ZYTE_API_KEY')
ZYTE_API_ENDPOINT = "https://api.zyte.com/v1/extract"

def scrape_website(url):
    try:
        response = requests.post(
            ZYTE_API_ENDPOINT,
            auth=(ZYTE_API_KEY, ""),
            json={
                "url": url,
                "browserHtml": True
            }
        )
        return response.json()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
```

### Exercise Files

1. **Network Capture Exercise** (`01_network_capture_exercise.py`)
   - Capture Nike API endpoints and product data
   - Configure API URLs and headers
   - Handle proxy configuration
   - Process and format product information
   - Save results in JSON format
   - Bonus tasks: pagination, filtering, metadata extraction

2. **Classic Pagination Exercise** (`02_pagination_classic_exercise.py`)
   - Scrape job listings from Indeed.com
   - Handle traditional page-by-page navigation
   - Extract job details (title, company, location)
   - Implement rate limiting and error handling
   - Bonus tasks: filters, CSV export, advanced search

3. **Infinite Scroll Exercise** (`03_infinite_scroll_exercise.py`)
   - Scrape Nike search results with infinite scroll
   - Handle dynamic content loading
   - Implement scroll timing and delays
   - Detect duplicate products
   - Bonus tasks: search filters, result rankings

4. **Form Submission Exercise** (`04_form_submission_exercise.py`)
   - Handle quote search form on quotes.toscrape.com
   - Multi-step form submission
   - Extract and validate results
   - Implement retry mechanisms
   - Bonus tasks: multiple form fields, export options

5. **Practice Scenarios** (`practice_scenarios.py`)
   - Additional real-world scenarios
   - Combine multiple techniques
   - Build complete scraping workflows
   - Focus on error handling and monitoring
   - Challenge exercises for advanced learning

Each exercise includes:
- Detailed instructions and TODOs
- Example implementations
- Error handling patterns
- Data processing examples
- Advanced bonus challenges

## Workshop Success Checklist
- [ ] All participants have working setup
- [ ] Basic scraper implementation successful
- [ ] Participants understand core concepts
- [ ] Questions addressed
- [ ] Next steps shared

## Next Steps
1. Advanced scraping techniques
2. Real-world case studies- Bring your own Usecases.
3. Performance optimization
4. Error handling best practices
5. Data storage solutions

## Support Resources
- Zyte API Signup: [link](https://www.zyte.com/zyte-api/?utm_campaign=DIS-ONBOARD&utm_activity=Community&utm_medium=social&utm_source=Discord&utm_content=zyte_api_Web32)
- Cursor IDE Download: [link](https://www.cursor.com/downloads)
- Workshop GitHub Repository: [link](https://github.com/NehaSetia-DA/zyte-api-training)

## 📚 Zyte API Documentation References

### Core Documentation
- [Getting Started Guide](https://docs.zyte.com/zyte-api/usage/index.html)
  - Complete overview of Zyte API
  - Basic concepts and setup
  - Authentication and configuration

### API Modes and Features
- [API Usage Examples](https://docs.zyte.com/zyte-api/usage/index.html#zapi-usage)
  - Common use cases
  - Code samples
  - Best practices

- [HTTP Mode](https://docs.zyte.com/zyte-api/usage/http.html)
  - Basic request handling
  - Headers and parameters
  - Response processing

- [Browser Mode](https://docs.zyte.com/zyte-api/usage/browser.html)
  - Browser automation
  - JavaScript rendering
  - Dynamic content handling

### Advanced Features
- [Browser Actions](https://docs.zyte.com/zyte-api/usage/browser.html#zapi-actions)
  - Click interactions
  - Form filling
  - Scrolling and navigation
  - Wait conditions

- [Extraction API](https://docs.zyte.com/zyte-api/usage/extract/index.html)
  - Data extraction methods
  - Selectors and filters
  - Response formats

- [Proxy Mode](https://docs.zyte.com/zyte-api/usage/proxy-mode.html)
  - Proxy configuration
  - IP rotation
  - Session handling

These documentation resources will be referenced throughout the workshop exercises and are essential for understanding the capabilities and proper usage of Zyte API.
