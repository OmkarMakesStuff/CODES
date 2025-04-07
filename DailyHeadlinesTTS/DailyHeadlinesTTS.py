import requests
import pyttsx3
from bs4 import BeautifulSoup

# Initialize the TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define function to read news
def readnews(top_article):
    speak(top_article['description'])

# Define function to summarize news (simply reading the same description for now)
def summarize(top_article):
    speak("Here's a summary of the article:")
    speak(top_article['description'])

# Function to read the full article content from URL
def read_full_article(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            paragraphs = soup.find_all('p')
            article_text = ' '.join(p.get_text() for p in paragraphs)
            print("\nFull Article:")
            print(article_text[:1500] + ('...' if len(article_text) > 1500 else ''))  # Preview
            speak("Here is the full article:")
            speak(article_text[:1500])  # To avoid very long speech, read first 1500 characters
        else:
            print("Could not fetch full article.")
    except Exception as e:
        print("Error reading article:", e)

# NewsAPI setup
api_key = '383ec47819f2482498afc50367111cf8'
categories = ['technology', 'business', 'entertainment', 'science', 'health', 'sports']
url = 'https://newsapi.org/v2/top-headlines'

print('Welcome to Daily Headlines!')
print('Please select a category:')
print('1. Technology')
print('Enter \'1\' for Technology')
print('Enter \'2\' for Business')
print('Enter \'3\' for Entertainment')
print('Enter \'4\' for Science')
print('Enter \'5\' for Health')
print('Enter \'6\' for Sports')
choice = input('Enter your choice: ')
choice = int(choice)
print('You have selected:', categories[choice - 1].capitalize())

params = {
    'apiKey': api_key,
    'country': 'us',
    'category': categories[choice - 1],
}

print('Fetching headlines...')
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    articles = data['articles']
    if articles:
        top_article = articles[0]
        print("\n\U0001F4F0 Top News:")
        print("Title:", top_article['title'])
        print("Description:", top_article['description'])
        print("URL:", top_article['url'])
        print('Do you want to hear the news? (yes/no)')
        hear_news = input('Enter your choice: ').strip().lower()
        if hear_news == 'yes':
            readnews(top_article)
      #   print('Do you want to hear the summary? (yes/no)')
      #   hear_summary = input('Enter your choice: ').strip().lower()
      #   if hear_summary == 'yes':
      #       summarize(top_article)
      #   print('Do you want to hear the full article? (yes/no)')
      #   hear_article = input('Enter your choice: ').strip().lower()
      #   if hear_article == 'yes':
      #       read_full_article(top_article['url'])
        else:
            
            print('Thank you for using Daily Headlines!')
        print('Have a great day!')
        exit()
    else:
        print("No articles found for this category.")
else:
    print("Failed to fetch news. Status code:", response.status_code)

print('Thank you for using Daily Headlines!')
print('Have a great day!')
