import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def clean_data(data):

    data['title'] = data['title'].str.strip()
    data['text'] = data['text'].str.strip()
    data['url'] = data['url'].str.strip()

    data['title'] = data['title'].str.lower()
    data['text'] = data['text'].str.lower()
    data['url'] = data['url'].str.lower()

    # clean deduplicate data
    data.drop_duplicates(subset=['title', 'text'], inplace=True)
    data.sort_values(by='publishDate', ascending=False, inplace=True)

    logger.info(data)
    logger.info("End of clean data:")
    return data
