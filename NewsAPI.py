from newsapi import NewsApiClient
from Article import Article
class NewsAPI:
    def __init__(self,category):
        self.category =  category
        self.client = NewsApiClient(api_key='5f4225f4585648c991449a7727488ca3')
        self.download_articles()

    def download_articles(self):
        self.articles=[Article(input) for input in self.client.get_everything(q=self.category,sort_by='popularity', language='en')['articles']]

    def get_titles_of_articles(self):
        return [article.get_title() for article in self.articles]
    
    def choose_article(self,articles):
        for art_num, article in enumerate(articles['articles']):
            print(art_num, ':  ', article['title'])
        return input('Which article would you like to see? ')

    def get_article_url(self,num):
        return self.articles[num].get_url()

    def get_article_summary(self,num):
        self.articles[num].print_summary()