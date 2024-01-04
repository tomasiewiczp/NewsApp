from newsapi import NewsApiClient
from Article import Article
from variables import API_KEY

class NewsAPI:
    def __init__(self,category):
        self.category =  category
        self.client = NewsApiClient(api_key = API_KEY)
        self.download_articles()

    def download_articles(self):
        self.articles=[Article(input) for input in self.client.get_everything(q=self.category,sort_by='popularity', language='en')['articles']]

    def get_titles_of_articles(self):
        return [article.get_title() for article in self.articles]

    def give_articles_details(self,title):
        for article in self.articles:
            if article.get_title()==title:
                return article.get_summary()