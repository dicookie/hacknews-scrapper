import os
import requests
from bs4 import BeautifulSoup
import csv
import datetime
import time

hackernews_url = 'https://thehackernews.com/'

def extract_articles(soup):
    result = []
    articles = soup.find_all('div', class_='body-post clear')
    for article in articles:
        title = article.find('h2', class_='home-title').text
        link = article.find('a')['href']
        description = article.find('div', class_='home-desc').text
        result.append([title, link, description])
    return result

def get_next_page_url(soup):
    next_button = soup.find('a', class_='blog-pager-older-link-mobile')
    if next_button:
        return next_button['href']
    return None

def scrape_hackernews():
    all_articles = []
    current_url = hackernews_url
    now = datetime.datetime.now()
    while current_url:
        response = requests.get(current_url)
        if response.status_code != 200:
            print(f'Failed to retrieve the webpage: {response.status_code}')
            break
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = extract_articles(soup)
        for article in articles:
            link = article[1]
            try:
                extracted_link = link.split('/')
                year = int(extracted_link[3])
                month = int(extracted_link[4])
                if year != now.year or month != now.month:
                    return all_articles
            except Exception as e:
                print(f"Error parsing date from URL: {e}")
                continue
        all_articles.extend(articles)
        current_url = get_next_page_url(soup)
        time.sleep(1)
    return all_articles

def save_to_csv(articles_data, filename):
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)     
    filepath = os.path.join(output_dir, filename)
    if os.path.exists(filepath):
        base, ext = os.path.splitext(filepath)
        filepath = base + '_update' + ext
    with open(filepath, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Link', 'Description'])
        writer.writerows(articles_data)
    print(f'Data saved to {filepath}')

if __name__ == '__main__':
    articles = scrape_hackernews()
    filename = f'hackernews_{datetime.date.today()}.csv'
    save_to_csv(articles, filename)
