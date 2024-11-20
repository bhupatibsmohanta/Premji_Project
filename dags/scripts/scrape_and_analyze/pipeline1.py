import logging
from scripts.scrape_and_analyze.fetch_articles import *
from scripts.scrape_and_analyze.clean_data import *
from scripts.scrape_and_analyze.generate_sentiment import *
from scripts.scrape_and_analyze.persist_data import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def scrape_and_analyze():
    try:
        data = fetch_articles()
        logger.info('Fetched articles successfully.')

        cleaned_data = clean_data(data)
        logger.info('Cleaned data successfully.')

        df = generate_sentiment(cleaned_data)
        logger.info('Generated sentiment successfully.')

        persist_data(df)
        logger.info('Persisted data successfully.')

    except Exception as e:
        logger.error(f'An error occurred: {str(e)}')

scrape_and_analyze()
