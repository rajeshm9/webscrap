#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 13:22:29 2019

@author: rajesh
"""
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import re
import sqlalchemy
import time
from bs4 import BeautifulSoup


url="https://www.usatoday.com/"
url="https://github.com/rajeshm9?tab=repositories"
url="https://www.naukri.com/devops-jobs"


'''
VERSION BUILD=1005 RECORDER=CR
URL GOTO=https://www.naukri.com/devops-jobs
TAB OPEN
TAG POS=1 TYPE=A ATTR=ID:jdUrl
TAG POS=1 TYPE=BUTTON ATTR=TXT:Next
'''

conn = sqlalchemy.create_engine('mysql+pymysql://root:raj#123@localhost/webscrap')
config = pd.read_sql_query("select * from config", conn) 

print(config)

options = Options()
#options.set_headless(headless=True)
#options.add_argument("--headless")
    
def getPageSrc (url):
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)
    
    src =  driver.page_source
    driver.close()
    return src

def readFromFile(fileName):
    with open(fileName, 'r') as content_file:
        return content_file.read()



def findallLinks(soup, link, next):
    
    d = config['mainlinkConfig'].str.split("|")[0]
    for a in soup.find_all(d[0], {d[1]: d[2]}):
        print(a.get('href'))
        
        
    d = config['mainlinkNextConfig'].str.split("|")[0]
    try:
        pageNext = soup.find(d[0], {d[1]: d[2]}).find("a").get('href')
        print(pageNext)
    except:
         pageNext = None
    
'''    
html_doc = getPageSrc(url)
file = open("tt.html", "w")
file.write(html_doc)
file.close()
'''

html_doc = readFromFile('tt.html')

soup = BeautifulSoup(html_doc, 'html.parser')


next = dict()

#findallLinks (soup, "a", "id", "jdUrl", "0")
findallLinks (soup, link, "0")
#findallLinks(soup, "a", "class", "js-asset-link", 0)
#findallLinks(soup, "a", "itemprop", "name codeRepository", 0)



      
