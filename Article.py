import logging
class Article:
    def __init__(self,article_data):
        self.article_data=article_data
        self.source=None
        self.author=None
        self.title=None
        self.description=None
        self.url=None
        self.urlToImage=None
        self.publishedAt=None
        self.content=None
        try:
            self.parse_data()
        except Exception as e:
            logging.error(f'Error while parsing data taken from NewsAPI client: {e}')

    def parse_data(self):
        self.source=self.article_data.get('source', {}).get('name')
        self.author= self.article_data.get('author', 'Unknown')
        self.title=self.article_data.get('title', 'Unknown')
        self.description=self.article_data.get('description', 'No description')
        self.url=self.article_data.get('url', 'No url')
        self.urlToImage=self.article_data.get('urlToImage', 'No image')
        self.publishedAt=self.article_data.get('publishedAt', 'No image')
        self.content=self.article_data.get('content', 'No content avalable')

    def get_title(self):
        return self.title
   
    def get_summary(self):
        """
        Returns a dictionary summary of the article.
        """
        summary_dict = {
            "Title": self.title,
            "Source": self.source,
            "URL": self.url
        }
        if self.author:
            summary_dict["Author"] = self.author
        if self.publishedAt:
            summary_dict["Published At"] = self.publishedAt
        if self.urlToImage:
            summary_dict["Image URL"] = self.urlToImage
        if self.description:
            truncated_description = self.description.split('[+')[0]
            summary_dict["Description"] = truncated_description
        return summary_dict
