# %%
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get the html content of the page
url = 'https://www.bbc.com/mundo/topics/c404v5gz1rkt'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Safari/537.36'
}

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Get articles with the following attributes: .card-body
articles = soup.find_all(class_="focusIndicatorDisplayBlock bbc-uk8dsi e1d658bg0")

# Get the URL of every article on the page with attributes "a"
urls = []

for article in articles[:10]:
    url = article['href']
    urls.append(url)
dates = []
elements = soup.find_all(class_="bbc-16jlylf e1mklfmt0")
for element in elements[:10]:
    dates.append(element.get_text())

information_list = []

# Get titles, subtitles, dates, and contents for every article
for index, link in enumerate(urls):

    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    # Get title
    title = soup.find(class_="bbc-14gqcmb e1p3vdyi0").get_text()

    # Get subtitle
    subtitle = soup.find(class_="bbc-hhl7in e17g058b0").get_text()

    content = []
    elements = soup.find_all(class_="bbc-hhl7in e17g058b0")
    for element in elements[1:-1]:
        content.append(element.get_text())

    information = {
        'date': dates[index],  # Use the corresponding date
        'Link': urls[index],
        'Website': 'BBC_Mundo',
        'title': title,
        'subtitle': subtitle,
        'content': content,
    }

    information_list.append(information)

# Create a DataFrame from the information list
df = pd.DataFrame(information_list)

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)





