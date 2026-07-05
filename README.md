# Browser Agent

A lightweight browser automation project built with **Python** and **Playwright**.

This project was created to learn browser automation by building a reusable controller and applying it to real web scraping tasks. Instead of writing Playwright code for every script, the project provides a simple `BrowserController` that wraps common browser actions.

## Features

* Open and navigate to web pages
* Click buttons and links
* Type into input fields
* Press keyboard keys
* Capture screenshots
* Extract text from web pages
* Retrieve multiple elements from a page
* Check whether page elements exist
* Get the current page URL
* Reusable browser controller for future automation projects

## Example Project

The repository includes a **Quote Scraper** built using the browser controller.

The scraper can:

* Visit https://quotes.toscrape.com
* Scrape quotes and authors
* Navigate through multiple pages
* Store scraped data in Python dictionaries
* Search quotes by author

Example output:

```python
[
    {
        "quote": "The world as we have created it is a process of our thinking...",
        "author": "Albert Einstein"
    },
    {
        "quote": "Try not to become a man of success. Rather become a man of value.",
        "author": "Albert Einstein"
    }
]
```

## Project Structure

```
Browser_Agent/
│
├── controller.py         # BrowserController implementation
├── quotescrapper.py      # Example quote scraper
├── Examplebot.py
├── searchbot.py
├── design_notes.md
└── README.md
```

## Technologies

* Python
* Playwright

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/Browser_Agent.git
cd Browser_Agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install playwright
playwright install
```

## Running the Quote Scraper

```bash
python quotescrapper.py
```

## What I Learned

This project helped me gain hands-on experience with:

* Browser automation
* Playwright
* Object-oriented programming
* Working with lists and dictionaries
* Building reusable Python classes
* Web scraping
* Pagination
* Debugging automation scripts

## Future Improvements

* Export scraped data to JSON or CSV
* Better error handling
* Waiting for dynamic page elements
* Headless browser support
* Additional example automation scripts

## License

This project is open source and available under the MIT License.
