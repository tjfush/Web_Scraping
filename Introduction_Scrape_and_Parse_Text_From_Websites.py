# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url)
page
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
#1st example
title_index = html.find("<title>")
title_index
start_index = title_index + len("<title>")
start_index
end_index = html.find("</title>")
end_index
title = html[start_index:end_index]
title

#2nd example, A bit messier
url = "http://olympus.realpython.org/profiles/poseidon"
page = urlopen(url)
html = page.read().decode("utf-8")
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
title

#Regular Expression (A more reliable option)

import re
re.findall("ab*c","ac") #using findall() to find any text within a string that matches the given regular expression
### '*' basically means zero or more of whatever comes before the asterisk, which either 'a', 'b' or both
re.findall("ab*c","abcd")
re.findall("ab*c","acc")
re.findall("ab*c","abcac")
re.findall("ab*c","abdc")
###Pattern matching is case sensitive. If you want to match this pattern regardless of the case, then you can pass a third argument with the value re.IGNORECASE
re.findall("ab*c","ABC")
###vs
re.findall('ab*c',"ABC", re.IGNORECASE)
### A period (.) stands for any single character in a regular expression
re.findall("a.c","abc")
re.findall("a.c","abbc")
re.findall("a.c","ac")
re.findall("a.c","acc")
### The pattern .* inside a regular expression stands for any character repeated any number of times
re.findall("a.*c","abc")
re.findall("a.*c","abbbbbbc")
re.findall("a.*c","ac")
re.findall("a.*c","acc")
#### Alernatively use re.search (which returns an object called MatchObject that stores different groups of data. We can retrieve our result by calling ".group" on our object)
match_results = re.search("ab*c","ABC", re.IGNORECASE)
match_results.group()
### Now on to substituting. re.suc()
string = "Everything is <replaced> if it's in <tags>."
string = re.sub("<.*>","ELEPHANTS", string)
string #Now because "*" has been used it searches for the first and last tag and our replacement ignores other tags in between. To limit this greed we use "*?" instead

string = "'Everything is <replaced> if it's in <tags>." 
string = re.sub("<.*?>","ELEPHANTS", string)
string #That does it

#Extract Text From HTML With Regular Expressions

from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = '<title.*?>.*?</title.*?>'
match_results = re.search(pattern,html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>","",title) #Remove HTML tags

print(title)
