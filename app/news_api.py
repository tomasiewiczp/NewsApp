import logging
from newsapi import NewsApiClient
from article import Article
from variables import API_KEY, DEFAULT_TO_NEWS_SITES

class NewsAPI:
    """
    A class that connects to the NewsAPI client, downloads articles based on a specified category,
    and provides methods to retrieve information about the articles.

    """

    def __init__(self, category=None):
        """
        Initializes the NewsAPI object with a specified category.
        It also initializes the NewsAPI client and downloads the articles.

        """
        self.category = category
        self.client = None
        self.articles = []
        self.initialize_client()
        self.get_sources()

    def initialize_client(self):
        """
        Initializes the NewsAPI client using the API key and handles any errors that occur during the connection.
        """
        try:
            self.client = NewsApiClient(api_key=API_KEY)
            if self.category:
                self.download_categorised_articles()
            else:
                self.download_main_articles()
        except Exception as e:
            logging.error(f'Error while connecting with NewsAPI client: {e}')
        self.remove_deleted_articles()

    def download_categorised_articles(self):
        """
        Downloads the articles from the NewsAPI client based on the specified category
        and handles any errors that occur during the download.
        """
        if self.client:
            try:
                response = self.client.get_top_headlines(category=self.category, language='en',page_size=100)
                self.articles = [Article(article_data) for article_data in response['articles']]
            except Exception as e:
                logging.error(f'Error while downloading articles from NewsAPI: {e}')

    def get_titles_of_articles(self):
        """
        Returns a list of the titles of the downloaded articles.
        """
        return [article.get_title() for article in self.articles]

    def get_articles_info(self):
        return [article.get_summary() for article in self.articles]
    
    def remove_deleted_articles(self):
        final_list=[]
        for article in self.articles:
            if not article.check_if_valid():
                final_list.append(article)
        self.articles=final_list

    def download_main_articles(self):
        chosen_sources = DEFAULT_TO_NEWS_SITES
        response = self.client.get_top_headlines(sources=chosen_sources, page_size=100)
        self.articles = [Article(article_data) for article_data in response['articles']]

    def get_sources(self):
        all_sources = self.client.get_sources()
        self.sources=[{'id':source['id'],'name':source['name']} for source in all_sources['sources']]





# cl=NewsAPI()
# print('test')
# cl.get_default_top_news()
