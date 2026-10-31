# PROJECT 04: WEB SCRAPER FOR QUOTES
import requests
import json
import time
from bs4 import BeautifulSoup
from collections import Counter
BASE = "https://quotes.toscrape.com"
HEADERS = {
    "User-Agent": "InternCircle-Learning-Project"
}
# Scrape quotes from multiple pages
def scrape_quotes():
    url = BASE + "/"
    quotes = []
    while url:
        try:
            response = requests.get(
                url,
                headers=HEADERS,
                timeout=10
            )
            response.raise_for_status()
            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )
            for item in soup.select("div.quote"):
                text = item.select_one("span.text")
                author = item.select_one("small.author")
                if text is None or author is None:
                    continue
                tags = [
                    tag.get_text(strip=True)
                    for tag in item.select("a.tag")
                ]
                quotes.append({
                    "text": text.get_text(strip=True),
                    "author": author.get_text(strip=True),
                    "tags": tags
                })
            next_page = soup.select_one("li.next a")
            if next_page:
                url = BASE + next_page["href"]
                time.sleep(1)
            else:
                url = None
        except requests.RequestException as error:
            print("Request error:", error)
            break
    return quotes
# Save quotes as JSON
def save_json(quotes):
    with open("quotes.json", "w", encoding="utf-8") as file:
        json.dump(
            quotes,
            file,
            indent=2,
            ensure_ascii=False
        )
    print("Quotes saved to quotes.json")
# Save quotes as text
def save_text(quotes):
    with open("quotes.txt", "w", encoding="utf-8") as file:
        for quote in quotes:
            file.write("Quote: " + quote["text"] + "\n")
            file.write("Author: " + quote["author"] + "\n")
            file.write(
                "Tags: " + ", ".join(quote["tags"]) + "\n"
            )
            file.write("-" * 50 + "\n")
    print("Quotes saved to quotes.txt")
# Display summary
def show_summary(quotes):
    if not quotes:
        print("No quotes were collected.")
        return
    authors = Counter(
        quote["author"] for quote in quotes
    )
    all_tags = []
    for quote in quotes:
        all_tags.extend(quote["tags"]
    tags = Counter(all_tags)
    print("\n===== SCRAPING SUMMARY =====")
    print("Total quotes:", len(quotes))
    if authors:
        print("Most quoted author:", authors.most_common(1)[0][0])
    if tags:
        print("Most common tag:", tags.most_common(1)[0][0])
# Main program
def main():
    print("===== WEB SCRAPER PROJECT =====")
    print("Starting quote collection...")
    quotes = scrape_quotes()
    if quotes:
        save_json(quotes)
        save_text(quotes)
        show_summary(quotes)
        print("\nScraping completed successfully!")
    else:
        print("No data collected. Please try again later.")
if __name__ == "__main__":
    main()
