# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 13:11:54 2022

@author: テンダイ ファッシャイ
"""

## How do you interact with HTML forms?
##  Use a third party package available from PyPI.
## MechanicalSoup is our guy.

# 1. Install Mechanical Soup in Terminal (do nothing here)

#CREATE BROWSER OBJECT
import mechanicalsoup
browser = mechanicalsoup.Browser()

url = "http://olympus.realpython.org/login"
page = browser.get(url)
page
#MechanicalSoup is built on Beautiful Soup
type(page.soup)
#To view the HTML

page.soup # the page has a login form

# Submit a Form with MechanicalSoup
##1
login_page = browser.get(url)
login_html = login_page.soup
##2
form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"
profiles_page = browser.submit(form, login_page.url)
profiles_page.url
#Let us obtain URLs of each link on our page
links = profiles_page.soup.select("a")

for link in links:
    address = link["href"]
    text = link.text
    print(f"{text}: {address}")
## Notice the addresses aren't full URLs, you need to concatenate them to the base URL

base_url = "http://olympus.realpytho.org"
for link in links:
    address = base_url + link["href"]
    text = link.text
    print(f"{text}: {address}")


## INTERACT WITH WEBSITES IN REAL TIME
#Let’s start by writing a simple program that opens the /dice page, scrapes the result, and prints it to the console:
import mechanicalsoup

browser = mechanicalsoup.Browser()
page = browser.get("http://olympus.realpython.org/dice")
tag = page.soup.select("#result")[0]
result = tag.text

print(f"The result of you dice roll is: {result}")

#Now let us run the page 4 times and collect the data

import time

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")
    time.sleep(10)
    
# To avoid runnin the programme for an extra  10 seconds we use an if statement to terminate the process
import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    result = tag.text
    print(f"The result of your dice roll is: {result}")

    # Wait 10 seconds if this isn't the last request
    if i < 3:
        time.sleep(10)