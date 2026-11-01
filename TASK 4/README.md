Project 04 – Web Scraper for Headlines & Quotes

Description

A Python web scraping application that collects quotes, authors and tags from a public practice website.

Website Used

https://quotes.toscrape.com

This website is specifically designed for practicing web scraping.

Features

- Sends HTTP requests using requests.
- Extracts HTML content using BeautifulSoup.
- Collects quotes, authors and tags.
- Scrapes multiple pages.
- Uses a one-second delay between page requests.
- Handles request errors.
- Saves collected information in JSON and TXT files.
- Displays total quotes, most quoted author and most common tag.

Libraries

- requests
- beautifulsoup4
- json
- time
- collections

Output Files

- quotes.json
- quotes.txt

Responsible Scraping

The project uses a public practice website, includes request timeouts and waits between page requests. It does not scrape personal data or login-protected pages.

Conclusion

This project demonstrates Python HTTP requests, HTML parsing, data extraction, JSON handling and file operations.
