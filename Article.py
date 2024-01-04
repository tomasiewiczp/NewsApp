class Article:
    def __init__(self,article_data):
        self.source=article_data['source']['name']
        self.author=article_data['author']
        self.title=article_data['title']
        self.description=article_data['description']
        self.url=article_data['url']
        self.urlToImage=article_data['urlToImage']
        self.publishedAt=article_data['publishedAt']
        self.content=article_data['content']

    def get_title(self):
        return self.title
    
    def get_url(self):
        return self.url
   
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
            # Przycinanie opisu, jeśli zawiera '[+'
            truncated_description = self.description.split('[+')[0]
            summary_dict["Description"] = truncated_description

        return summary_dict
