import requests
from bs4 import BeautifulSoup

url = "https://www.thehindu.com/news/national/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headlines = soup.find_all("h3")

headline_title = []

for h in headlines:
    text = h.get_text(strip=True)
    if len(text) > 6:
      headline_title.append(text)

with open("headlines.txt","w",encoding="utf-8") as f:
    for line in headline_title:
        f.write(line+"\n")

print("Scraping Completed....")