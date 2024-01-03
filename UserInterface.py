from NewsAPI import NewsAPI
import webbrowser
class UserInterface:
    def __init__(self):
        self.categories =  ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    
    def create_newsAPI_client(self,category):
        self.newsAPIclient= NewsAPI(category)

    def choose_categories_and_create_client(self):
        print("CATEGORIES")
        for i, category in enumerate(self.categories):
            print(f"{i}: {category}")

        choice = int(input("Choose your category: "))
        self.create_newsAPI_client(self.categories[choice])

    def choose_article(self):
        articles=self.newsAPIclient.get_titles_of_articles()
        for art_num, article in enumerate(articles):
            print(art_num, ':  ', article)
        return input('Which article would you like to see? ')

    def show_or_enter_the_article(self):
        article_num = int(self.choose_article())
        decision = input('Would you like to open the article in browser (O), read the summary (R) or quit this list (Q)? ').upper()
        if decision == 'O':
            url = self.newsAPIclient.get_article_url(int(article_num))
            webbrowser.open(url)
            return True
        elif decision == 'R':
            self.newsAPIclient.get_article_summary(int(article_num))
            return True
        elif decision == 'Q':
            return False