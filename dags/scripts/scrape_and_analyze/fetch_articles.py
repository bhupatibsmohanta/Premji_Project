import requests
import json
import pandas as pd
import datetime
from bs4 import BeautifulSoup
import hashlib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def fetch_articles():

    query = ["HDFC","Tata Motors"]

    article_df_final = pd.DataFrame(columns=['aid','source','type','title','url','publishDate','text','query'])
    for each_query in query:
        article_df = pd.DataFrame(columns=['aid','source','type','title','url','publishDate','text'])
        r = requests.get(url="https://backend.finshots.in/backend/search/?q="+each_query)
        out = json.loads(r.content)
        matches = out['matches']
        for match in matches:
            title = match['title']
            publishDate = datetime.datetime.strptime(match['published_date'].split('T')[0],"%Y-%m-%d").date().strftime('%Y-%m-%d')
            url = match['post_url']
            req = requests.get(url=url)
            soup = BeautifulSoup(req.content, 'lxml')
            p_tags = soup.find_all('div',{"class":"post-content"})
            text = ""
            hash_obj = hashlib.sha256(url.encode('utf-8'))
            hex_hash = hash_obj.hexdigest()
            aid = str(hex_hash)
            for p in p_tags:
                text+=p.text
            article_df = pd.concat([article_df, pd.DataFrame([[aid,'FinShots','Article',title,url,publishDate,text,each_query]],columns=['aid','source','type','title','url','publishDate','text','query'])],ignore_index=True)

        article_df.sort_values(by='publishDate', ascending=False, inplace=True)
        first_five_records = article_df.head(5)
        article_df_final = pd.concat([article_df_final,first_five_records],ignore_index=True)
    
    logger.info(f"Fetched {len(article_df_final)} articles")
    
    return article_df_final

fetch_articles()
