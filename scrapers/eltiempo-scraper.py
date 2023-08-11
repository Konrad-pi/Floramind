# Webscraper for https://www.eltiempo.com/colombia
# Author: Manuel Davy Ntsoumou + Konrad von Klitzing

import requests
from IPython.display import display
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Get the html content of the page
url = 'https://www.eltiempo.com/colombia'
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36'
}

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Get articles with the following attributes itemprop='headline'
articles = soup.find_all(itemprop='headline')

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

print(urls)

# get titles, subtitles, dates and contents for every article
for link in urls:

    r = requests.get("https://www.eltiempo.com/" + link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    #get title
    title = soup.select_one(".titulo-principal-bk .titulo").get_text()

    #get subtitle
    subtitle = soup.select_one(".article-epigraph").get_text()
    
    #get date  
    date = soup.select(".publishedAt")[2].get_text()


    #get content from paragraphs
    content = []
    paragraphs = soup.select("p")

    for p in paragraphs:
       content.append(p.get_text())
    
    information = {
    'date': date,
    'link': "https://www.eltiempo.com" + link,
    'title': title,
    'subtitle': subtitle,
    'content': content,
    }

    information_list.append(information)


df = pd.DataFrame(information_list)

display(df)

# Save the data in a csv file
current_date = datetime.datetime.now()
filename =  str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '-' + 'eltiempo'
df.to_csv(str(filename + '.csv'))

print("done!")
