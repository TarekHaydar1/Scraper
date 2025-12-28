# Web Scraper with AI Analysis

An intelligent web crawler that extracts content from websites and uses OpenAI's GPT models to analyze and summarize the information.

## Overview

This tool combines web crawling capabilities with AI-powered content analysis. It crawls a target website, extracts all internal pages, converts them to markdown format, and then uses OpenAI's GPT-4o-mini model to intelligently extract and summarize key information from the crawled content.

## Features

- **Async Web Crawling**: Efficiently crawls websites using `crawl4ai` with async/await patterns
- **Internal Link Discovery**: Automatically discovers and crawls all internal links from the starting URL
- **Cookie-Based Authentication**: Supports authenticated crawling with custom cookies
- **Markdown Extraction**: Converts HTML pages to clean markdown format for better AI processing
- **AI-Powered Analysis**: Uses OpenAI GPT-4o-mini to intelligently extract and summarize information
- **User Simulation**: Simulates real user behavior for better content extraction

## How It Works

1. **Initial Crawl**: Starts by crawling the base website URL
2. **Link Discovery**: Extracts all internal links from the initial page
3. **Parallel Crawling**: Crawls all discovered internal links concurrently
4. **Content Extraction**: Converts all crawled pages to markdown format
5. **AI Analysis**: Sends the markdown content to OpenAI GPT-4o-mini for intelligent analysis
6. **Information Extraction**: The AI model extracts and summarizes key information based on user queries

## Requirements

- Python 3.7+
- `crawl4ai` - Web crawling library
- `openai` - OpenAI API client
- `python-dotenv` - Environment variable management

## Installation

```bash
pip install crawl4ai openai python-dotenv
```

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Browser Configuration

The crawler supports custom browser configuration including:
- **Cookies**: For authenticated sessions (sessionid, csrftoken, etc.)
- **Wait Strategy**: Configurable wait conditions (e.g., `domcontentloaded`)
- **User Simulation**: Simulates real user interactions
- **Cache Mode**: Bypass cache for fresh content

### Example Configuration

```python
browser_conf = BrowserConfig(
    cookies=[
        {
            "name": "sessionid",
            "value": "xxx",
            "domain": "example.com",
            "path": "/"
        }
    ]
)

run_conf = CrawlerRunConfig(
    wait_until="domcontentloaded",
    simulate_user=True,
    cache_mode=CacheMode.BYPASS
)
```

## Usage

1. Set your OpenAI API key in the `.env` file
2. Update the target website URL in the code
3. Configure browser settings (cookies, etc.) if needed
4. Run the script:

```bash
python Crawler.py
```

## Code Structure

- `main()`: Async function that handles the crawling process
  - Crawls the initial website
  - Discovers internal links
  - Crawls all links in parallel
  - Returns all crawled pages as markdown

- **AI Analysis**: After crawling, the script:
  - Sends all markdown content to OpenAI
  - Uses a system prompt to guide the AI's analysis
  - Processes user queries to extract specific information

## Example Use Case

The current implementation crawls `edwarddonner.com` and asks the AI to extract information about "Ed". The AI model analyzes all crawled pages and provides a comprehensive summary based on the content found.

## Customization

You can easily customize:
- **Target Website**: Change the `Website` variable
- **AI Model**: Modify `MODEL_GPT` (e.g., 'gpt-4o-mini', 'gpt-4', etc.)
- **System Prompt**: Adjust the prompt to change how the AI analyzes content
- **User Query**: Change `User_prompt` to ask different questions about the crawled content

## Notes

- The crawler respects the website's structure and only follows internal links
- Cookie authentication is required for some websites
- The AI analysis works best with well-structured markdown content
- Large websites may take time to crawl completely

## License

This project is open source and available for use.
