import logging
from newsapi import NewsApiClient
from article import Article
from variables import API_KEY

class NewsAPI:
    """
    A class that connects to the NewsAPI client, downloads articles based on a specified category,
    and provides methods to retrieve information about the articles.

    """

    def __init__(self, category):
        """
        Initializes the NewsAPI object with a specified category.
        It also initializes the NewsAPI client and downloads the articles.

        """
        self.category = category
        self.client = None
        self.articles = []
        self.initialize_client()

    def initialize_client(self):
        """
        Initializes the NewsAPI client using the API key and handles any errors that occur during the connection.
        """
        try:
            self.client = NewsApiClient(api_key=API_KEY)
            self.download_articles()
        except Exception as e:
            logging.error(f'Error while connecting with NewsAPI client: {e}')
        self.delete_yahoo_articles()

    def download_articles(self):
        """
        Downloads the articles from the NewsAPI client based on the specified category
        and handles any errors that occur during the download.
        """
        if self.client:
            try:
                response = self.client.get_everything(q=self.category, sort_by='popularity', language='en')
                self.articles = [Article(article_data) for article_data in response['articles']]
            except Exception as e:
                logging.error(f'Error while downloading articles from NewsAPI: {e}')

    def get_titles_of_articles(self):
        """
        Returns a list of the titles of the downloaded articles.
        """
        return [article.get_title() for article in self.articles]

    def give_articles_details(self, title):
        """
        Returns the details of a specific article based on its title.
        """
        for article in self.articles:
            if article.get_title() == title:
                return article.get_summary()
    
    def get_articles_base_info(self):
        return [{'title':article.get_summary()['Title'],'photo_url':article.get_summary()["Image URL"]} for article in self.articles]
    
    def delete_yahoo_articles(self):
        final_list=[]
        for article in self.articles:
            if not article.check_if_yahoo():
                final_list.append(article)
        self.articles=final_list