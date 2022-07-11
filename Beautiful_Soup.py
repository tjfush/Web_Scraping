# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:04:46 2022

@author: テンダイ ファッシャイ
"""
#Use an HTML Parser for Web Scrapping in Python


# https://realpython.com/python-web-scraping-practical-introduction/#use-an-html-parser-for-web-scraping-in-python
#Install Beautiful Soup in terminal through Shell

## Create a BeautifulSoup Object

from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)

html = page.read().decode("utf-8")

soup = BeautifulSoup(html, "html.parser")
print(soup.get_text())
 #To find instances of a particular tag e.g. images (<img>)
soup.find_all("img") # A list of the 2 Tag objects is outputed 
#Unpack the Tag objects you find.

image1, image2 = soup.find_all("img")
#Check the tag type using the '.name' property
image1.name

# Check HTML attributes

image1["src"]
image2["src"]

#Let us try another one

soup.title #still kinda messy, but the idea is there
soup.title.string
# Let us search for all instances of a specific tag

soup.find_all("img", src="/static/dionysus.jpg")

