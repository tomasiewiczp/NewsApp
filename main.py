from NewsAPI import NewsAPI 
from UserInterface import UserInterface

# Main application flow
interface=UserInterface()

app_going = interface.choose_categories_and_create_client()
while app_going:
    app_going = interface.show_or_enter_the_article()