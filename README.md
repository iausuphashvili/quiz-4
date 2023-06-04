Web Scraper - Quotes to CSV

This Python script is designed to scrape quotes from the website "https://quotes.toscrape.com" and save them to a CSV file. It utilizes the requests library to fetch the HTML content of each page, and the BeautifulSoup library to parse the HTML and extract the desired data. The extracted quotes, along with their respective authors and tags, are then stored in a CSV file using the csv module.

The script loops through multiple pages of the website (in this case, from page 1 to page 5) and extracts the necessary information from each quote block. It retrieves the quote text, author name, and associated tags. These details are appended to a list of rows, which will later be written to the CSV file.

To ensure polite scraping and avoid overwhelming the server, the script includes a delay of 15 seconds between each page request using the time.sleep() function.

Once all the quotes have been scraped and stored in the rows list, they are written to a CSV file named data.csv using the csv.writer() object. The resulting CSV file will have four columns: "Page" (indicating the page number the quote was found on), "Quote" (the text of the quote), "Author" (the author of the quote), and "Tags" (a space-separated list of tags associated with the quote).