from NewsAPI import NewsAPI
import webbrowser
import requests

class UserInterface:
    def __init__(self):
        self.categories =  ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    
    def create_newsAPI_client(self,category):
        self.newsAPIclient = None
        try:
            self.newsAPIclient = NewsAPI(category)
        except requests.exceptions.HTTPError as e:
            print(f" HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            print("Connection error")
        except requests.exceptions.Timeout:
            print("timeout error")
        except requests.exceptions.RequestException as e:
            print(f"request error: {e}")

    def choose_categories_and_create_client(self):
        print("CATEGORIES")
        for i, category in enumerate(self.categories):
            print(f"{i}: {category}")
        try:
            choice = int(input("Choose your category: "))
            self.create_newsAPI_client(self.categories[choice])
        except ValueError:
            print("Wrong number")
        except IndexError:
            print("Too big (or small) number")
        if self.newsAPIclient:
            return True
        else:
            return False

    def choose_article(self):
        articles=self.newsAPIclient.get_titles_of_articles()
        for art_num, article in enumerate(articles):
            print(art_num, ':  ', article)
        return input('Which article would you like to see? (Q) for exit ')

    def show_or_enter_the_article(self):
        input()
        choice=self.choose_article()
        if not choice.isdigit():
            return False
        article_num = int(choice)
        decision = input('Would you like to open the article in browser (O), read the summary (R) or quit this list (Q)? ').upper()
        if decision == 'O':
            url = self.newsAPIclient.get_article_url(int(article_num))     
            try:
                url = self.newsAPIclient.get_article_url(int(article_num))
                webbrowser.open(url)
                return True
            except webbrowser.Error:
                print("Unable to open the website")
        elif decision == 'R':
            self.newsAPIclient.get_article_summary(int(article_num))
            return True
        elif decision == 'Q':
            return False