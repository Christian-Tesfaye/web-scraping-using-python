import requests
import time 
from bs4 import BeautifulSoup

url = "https://ethiopianmonitor.com/category/news/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

articles = soup.find_all("article")

def print_with_time_interval(res, interval):
 for article in articles:
  
    title = article.find("h2").text.strip()
    date_element =article.find("span",class_="cm-post-date human-diff-time-display").text.strip()
    description_element = article.find("div", class_="cm-entry-summary").text.strip()
    image_url = article.find("img")["src"] if article.find("img") else "Image URL not found"
    link=article.find("a",class_="cm-entry-button")["href"]
    
    if date_element:
        date = date_element
    else:
        date = "Date not available"

    if description_element:
        description = description_element
    else:
        description = "Description not available"

    bot_token = 'botid'
    channel_id = 'chatid'

   
    url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
    params = {
        'chat_id': channel_id,
        'photo': image_url,
        'caption': f"{title}\n\n{date_element}\n\n {description_element}\n{link}"
    }
    response = requests.get(url, params=params)
    res=response.json()
    print(res)
    time.sleep(interval)

print_with_time_interval(response.json, 10)
