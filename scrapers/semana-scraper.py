# Webscraper for https://www.semana.com/nacion/
# Author: Manuel Davy Ntsoumou + Konrad von Klitzing

import requests
from IPython.display import display
from bs4 import BeautifulSoup
import pandas as pd
import datetime

# Get the html content of the page
url = 'https://www.semana.com/nacion/'
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36'
}

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Get articles with the following attributes .card-body
articles = soup.find_all(class_='card-body')

# Get the URL of every article on the page with attributes a using pandas
urls = []

# Set counter + article_max to limit the number of articles
counter = 0
article_max = 5

for article in articles:
    # limit to 'article_max' articles
    if counter == article_max:
        break
    
    url = article.find('a')['href']
    urls.append(url)

    counter += 1


# print(urls)

information_list = []

# get titles, subtitles, dates and contents for every article
for link in urls:

    r = requests.get("https://www.semana.com/" + link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #get title
    title = soup.select_one(".lg\:text-4xl").get_text()
    #print(title)

    #get subtitle
    subtitle = soup.select_one("p.mb-4.text-lg").get_text()
    #print(subtitle)
    
    #get date  
    date = soup.select_one(".pl-2.text-xs.leading-none").get_text()
    #print(date)

    content = []
    paragraphs = soup.select(".max-w-screen-md p")

    for p in paragraphs:
        content.append(p.get_text())
    #print(content)

    information = {
    'date': date,
    'link': "https://www.semana.com" + link,
    'title': title,
    'subtitle': subtitle,
    'content': content,
    'source': 'semana'
    }


    information_list.append(information)    

df = pd.DataFrame(information_list)

display(df)

# Save the data in a csv file
current_date = datetime.datetime.now()
filename =  str(current_date.year) + '-' + str(current_date.month) + '-' + str(current_date.day) + '-' + 'semana'
df.to_csv(str(filename + '.csv'))

print("done!")