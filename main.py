import requests
import webbrowser
from newsapi import NewsApiClient

# List of available categories
categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
# Initialize the NewsAPI client with the API key
newsapi = NewsApiClient(api_key='5f4225f4585648c991449a7727488ca3')

def choose_categories():
    """
    Displays the list of categories and prompts the user to choose one.
    Returns the selected category.
    """
    print("CATEGORIES")
    for i, category in enumerate(categories):
        print(f"{i}: {category}")

    choice = int(input("Choose your category: "))
    return categories[choice]

def download_articles(selected_category):
    """
    Downloads the top headlines for the selected category.
    Args:
    selected_category (str): The category chosen by the user.
    
    Returns:
    dict: The top headlines from the NewsAPI.
    """
    top_headlines = newsapi.get_top_headlines(category=selected_category, language='en')
    return top_headlines

def choose_article(articles):
    """
    Displays the list of articles and prompts the user to choose one.
    Args:
    articles (dict): The articles returned by the NewsAPI.
    
    Returns:
    str: The index of the selected article.
    """
    for art_num, article in enumerate(articles['articles']):
        print(art_num, ':  ', article['title'])
    return input('Which article would you like to see? ')

def show_or_enter_the_article(articles, selected_article):
    """
    Prompts the user to open the article in a browser, read the summary, or quit.
    Args:
    articles (dict): The articles returned by the NewsAPI.
    selected_article (str): The index of the selected article.
    
    Returns:
    bool: True if the app should continue, False if the user chooses to quit.
    """
    decision = input('Would you like to open the article in browser (O), read the summary (R) or quit this list (Q)? ').upper()
    if decision == 'O':
        url = articles['articles'][int(selected_article)]['url']
        webbrowser.open(url)
        return True
    elif decision == 'R':
        print('Title: ', articles['articles'][int(selected_article)]['title'])
        print('Author: ', articles['articles'][int(selected_article)]['author'])
        print('Description: ', articles['articles'][int(selected_article)]['description'])
        return True
    elif decision == 'Q':
        return False

# Main application flow
selected_category = choose_categories()
articles = download_articles(selected_category)
selected_article = choose_article(articles)

app_going = True
while app_going:
    app_going = show_or_enter_the_article(articles, selected_article)