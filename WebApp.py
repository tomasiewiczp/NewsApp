from flask import Flask, render_template
from variables import CATEGORIES
from NewsAPI import NewsAPI
import requests

class WebApp:
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

    def __init__(self):
        self.app = Flask(__name__)
        self.categories =  CATEGORIES
        self.newsAPIclient = None

        @self.app.route('/')
        def home():
            return render_template('home.html')

        @self.app.route('/categories')
        def categories():
            return render_template('categories.html', categories = self.categories)

        @self.app.route('/category/<category_name>')
        def show_category(category_name):
            self.create_newsAPI_client(category_name)
            titles = self.newsAPIclient.get_titles_of_articles()
            return render_template('articles.html', titles=titles)

        @self.app.route('/articles/<title>')
        def show_article_details(title):
            return render_template('article_details.html', title=title,details=self.newsAPIclient.give_articles_details(title))
        
    def run(self):
        self.app.run(debug=True)