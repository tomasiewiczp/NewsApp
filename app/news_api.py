import logging
from newsapi import NewsApiClient
from article import Article
from variables import API_KEY

class NewsAPI:
    def __init__(self,category):
        self.category = category
        self.client = None
        self.articles = []
        self.initialize_client()

    def initialize_client(self):
        try:
            self.client = NewsApiClient(api_key=API_KEY)
            self.download_articles()
        except Exception as e:
            logging.error(f'Error while connecting with NewsAPI client: {e}')

    def download_articles(self):
        if self.client:
            try:
                response = self.client.get_everything(q=self.category, sort_by='popularity', language='en')
                self.articles = [Article(article_data) for article_data in response['articles']]
            except Exception as e:
                logging.error(f'Error while downloading articles from NewsAPI: {e}')

    def get_titles_of_articles(self):
        return [article.get_title() for article in self.articles]

    def give_articles_details(self,title):
        for article in self.articles:
            if article.get_title()==title:
                return article.get_summary()