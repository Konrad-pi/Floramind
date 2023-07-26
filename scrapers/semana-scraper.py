# Webscraper for https://www.semana.com/nacion/
# Author: Manuel Davy Ntsoumou + Konrad von Klitzing

import requests
from bs4 import BeautifulSoup
import pandas as pd

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
for article in articles:
    url = article.find('a')['href']
    urls.append(url)


# print(urls)


information_list = []

# get titles, subtitles, dates and contents for every article
for link in urls:

    r = requests.get("https://www.semana.com/" + link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    #get title
    title = soup.select(".lg\:text-4xl")
    #print(title)

    #get subtitle
    subtitle = soup.select(".max-w-\[968px\] .mb-5")
    #print(subtitle)
    
    #get date  
    date = soup.select(".pl-2.text-xs.leading-none")
    print(date)

    content = []
    paragraphs = soup.find_all('p')

    for p in paragraphs:
        content.append(p.get_text())
    #print(content)

    information = {
    'date': date,
    'title': title,
    'subtitle': subtitle,
    'content': content,
    }


    # information_list.append(information)
    # display(information)

    break

