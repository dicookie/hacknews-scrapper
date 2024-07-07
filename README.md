# The Hacker News Web Scraper

This is a Python script that scrapes articles from [The Hacker News](https://thehackernews.com) for the current month. The script iterates through pages and collects titles, links, and descriptions of articles in this month.

## How to Use

1. Clone the repository or download the script file:

    ```sh
    git clone https://github.com/dicookie/hacknews-scrapper
    cd hacknews-scrapper
    ```

2. Install the required libraries:

    ```sh
    pip install requests beautifulsoup4
    ```

3. Run the script:

    ```sh
    python scrape_hackernews.py
    ```

##

The script will scrape the current month's articles and save them to a CSV file in the `output` directory. If a file with the same name already exists, the new file will be saved with `_updated` appended to the filename.

Happy Reading!
