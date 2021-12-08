from GoogleNews import GoogleNews
from newspaper import Article
from newspaper import Config
from datetime import date
import pandas as pd
import nltk
import requests
nltk.download('punkt')

def newsextract(URL):
    user_agent = 'Chrome/50.0.2661.102'
    config = Config()
    config.browser_user_agent = user_agent
    raw_html = requests.get(URL, verify=False)
    article = Article('')
    article.download(raw_html.content)
    article.parse()
    article.nlp()
    title = article.title
    publish_date = article.publish_date
    text = article.text
    keywords = article.keywords
    return title,publish_date,text,keywords