from variables import CATEGORIES
from news_api import NewsAPI
import requests
from flask import Flask, render_template, abort, redirect, url_for
import logging
class WebApp:
    def create_newsAPI_client(self,category):
        self.newsAPIclient = None
        try:
            self.newsAPIclient = NewsAPI(category)
        except requests.exceptions.HTTPError as e:
            logging.error(f" HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            logging.error(f"Connection error: {e}")
        except requests.exceptions.Timeout:
            logging.error(f"timeout error: {e}")
        except requests.exceptions.RequestException as e:
            logging.error(f"request error: {e}")
        except Exception as e:
            logging.error(f"error: {e}")

    def __init__(self):
        self.app = Flask(__name__)
        self.categories =  CATEGORIES
        self.newsAPIclient = None
        self.init_routes()

    def init_routes(self):
            @self.app.route('/')
            def home():
                try:
                    return render_template('home.html')
                except Exception as e:
                    logging.error(f"Error rendering home template: {e}")
                    return "Error rendering the page", 500

            @self.app.route('/category/<category_name>')
            def show_category(category_name):
                if category_name not in self.categories:
                    abort(404) 
                self.create_newsAPI_client(category_name)
                if self.newsAPIclient:
                    titles = self.newsAPIclient.get_titles_of_articles()
                    return render_template('articles.html', titles=titles)
                else:
                    return "Error loading articles", 500

            @self.app.route('/articles/<title>')
            def show_article_details(title):
                details = self.newsAPIclient.give_articles_details(title)
                if details:
                    return render_template('article_details.html', title=title, details=details)
                else:
                    return redirect(url_for('home'))

            @self.app.errorhandler(404)
            def page_not_found(e):
                return render_template('404.html'), 404

            @self.app.route('/categories')
            def categories():
                if self.categories:
                    try:
                        return  render_template('categories.html', categories = self.categories)
                    except Exception as e:
                        logging.error(f"Error rendering home template: {e}")
                        return "Error rendering the page", 500
                else:
                    return redirect(url_for('home'))

    def run(self):
        self.app.run(debug=True)