# Webscraper for https://cnnespanol.cnn.com/category/zona-andina/colombia/
# Author: Manuel Davy Ntsoumou + Konrad von Klitzing

import requests
import re
from IPython.display import display
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Get the html content of the page
url = 'https://cnnespanol.cnn.com/category/zona-andina/colombia/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

}

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Get articles with the following attributes itemprop='headline'
articles = soup.find_all(class_='news__title')

# Get the URL of every article on the page with attributes a using pandas
urls = []

# Set counter + article_max to limit the number of articles
counter = 0
article_max = 10

for article in articles:
    # limit to 'article_max' articles
    if counter == article_max:
        break
    
    url = article.find('a')['href']
    urls.append(url)

    counter += 1

# print urls
information_list = []

# get titles, subtitles, dates and contents for every article
for link in urls:

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    #get title
    title = soup.find("h1").get_text().strip()
    #print(title)
        
    # Get date  (COMPLICATED!)
    date = soup.find(class_='news__date')
    if date == None:
        date = soup.find(class_='storyfull__time')

    date = date.get_text()
    clean_date = re.sub(r'\s+', ' ', date).strip()

    # Remove the time from the string
    clean_date = re.sub(r'\(\d+:\d+\s+\w+\)', '', clean_date)

    # Extract the day, month, and year using regular expressions
    day, month, year = re.search(r'(\d+).+(\w+),\s+(\d+)', clean_date).groups()
    
    #get content from paragraphs
    content = []
    paragraphs = soup.select("p")

# exclude the last paragraph, which is not part of the article
    for p in paragraphs[3:-1]:
        content.append(p.get_text().strip())
    
    information = {
    'date': clean_date,
    'link': link,
    'title': title,
    'content': content,
    }

    information_list.append(information)

df = pd.DataFrame(information_list)

# Save the data in a csv file
current_date = datetime.datetime.now()
filename =  str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '-' + 'cnnespanol'
df.to_csv(str(filename + '.csv'))

print("done!")