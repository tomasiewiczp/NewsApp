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
    
    def print_summary(self):
        """
        Prints a formatted summary of the article.
        """
        print("------------------------------------------------")
        print(f"Title: {self.title}")
        print(f"Source: {self.source}")
        if self.author:
            print(f"Author: {self.author}")
        if self.publishedAt:
            print(f"Published At: {self.publishedAt}")
        print(f"URL: {self.url}")
        if self.urlToImage:
            print(f"Image URL: {self.urlToImage}")
        if self.description:
            print(f"Description: {self.description}")
        if self.content:
            print(f"Content: {self.content}")
        print("------------------------------------------------")