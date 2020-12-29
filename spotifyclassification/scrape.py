import requests
from bs4 import BeautifulSoup
import math

import requests
from bs4 import BeautifulSoup
import random
import re
 
text = 'top 100 happy songs of all time'
url = 'https://google.com/search?q=' + text

'''
get titles for top songs on google results
'''
# A = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
#        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
#        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
#        )
A = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
# Agent = A[random.randrange(len(A))]
Agent = A 
headers = {'user-agent': Agent}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, 'lxml')
for info in soup.find_all('div', attrs={"class":"title"}):
# for info in soup.find_all('h3'):
    print(info.text)
    print('#######')

'''
get the links on google results page
'''
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'lxml')
# links = soup.findAll("a")
# for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
#     print(re.split(":(?=http)",link["href"].replace("/url?q=","")))










# user_input = handle_casing(user_input)
# url = "https://www.google.com/search?ei=PfHcX9nVKJqQtAbH9pf4Cw&q=top+100+sad+songs+of+all+time&oq=top+100+sad+songs+of+all+time&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR1CvBFivBGC9CWgAcAJ4AIABAIgBAJIBAJgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwiZ6KyAkdjtAhUaCM0KHUf7Bb8Q4dUDCA4&uact=5"
# response = requests.get(url)
# # soup = BeautifulSoup(response.text, 'html.parser')
# # script = soup.find('pre')
# html = response.content
# tree = BeautifulSoup(html, features="lxml")
# good_html = tree.prettify()
# soup = BeautifulSoup(good_html, "html5lib")
# results = soup.find_all('div', attrs={"class":"title"})
# print(results)

# allScript = script.getText
# everyBody = script.findAll("title") #possible indictors of a scene
# print(everyBody)
# import urllib
# import requests
# from bs4 import BeautifulSoup

# query = "hackernoon How To Scrape Google With Python"
# query = query.replace(' ', '+')
# URL = f"https://google.com/search?q={query}"

# # desktop user-agent
# USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
# headers = {"user-agent" : USER_AGENT}
# resp = requests.get(URL, headers=headers)

# if resp.status_code == 200:
#     soup = BeautifulSoup(resp.content, "html.parser")

#     results = []
#     for g in soup.find_all('div', class_='r'):
#         anchors = g.find_all('a')
#         if anchors:
#             link = anchors[0]['href']
#             title = g.find('h3').text
#             item = {
#                 "title": title,
#                 "link": link
#             }
#             results.append(item)
#     print(results)