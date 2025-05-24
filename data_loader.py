import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_sample_messages():
    url = "https://www.fakepersongenerator.com/email-text-generator"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    messages = [tag.get_text() for tag in soup.find_all('div', class_='email-text')]
    return messages if messages else ["Default fallback message if scraping fails"]

def load_sms_dataset():
    url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
    df = pd.read_csv(url, sep='\t', header=None, names=['label', 'message'])
    scraped_messages = scrape_sample_messages()
    scraped_df = pd.DataFrame(scraped_messages, columns=['message'])
    scraped_df['label'] = 'unknown'  # Label for clustering only
    df = pd.concat([df, scraped_df], ignore_index=True)
    return df
