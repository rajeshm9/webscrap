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
import re


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
                                
                                
config = pd.read_sql_query("select * from config where status='A'", conn) 


options = Options()
#options.set_headless(headless=True)
#options.add_argument("--headless")
    
def getPageSrc (url):
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)
    
    src =  driver.page_source
    driver.close()
    
    file = open("debug.html", "w")
    file.write(src)
    file.close()
    
    return src

def readFromFile(fileName):
    with open(fileName, 'r') as content_file:
        return content_file.read()


def pageInfo(url, row):
    
    html_doc = getPageSrc(url)
    soup = BeautifulSoup(html_doc, 'html.parser')
    d = row['sublinkTitle'].split("|")
    try:
        sublinkTitle = soup.find(d[0], {d[1]: d[2]}).get_text()
        print(sublinkTitle)
    except:
         sublinkTitle = None
    
def findallLinks(soup, row):
    
    d = row['mainlinkConfig'].split("|")
    if d[0] == 'a':
        for a in soup.find_all(d[0], {d[1]: d[2]}):
            sublink =(a.get('href'))
            print(sublink)
            break    
    else:
        for a in soup.find_all(d[0], {d[1]: d[2]}):
            sublink =(a.find('a').get('href'))
            print(sublink)
            break 
        
    if re.match('^http', sublink) == None:
        sublink = row['baseUrl'] + sublink
        
    pageInfo(sublink, row)
    
    d = row['mainlinkNextConfig'].split("|")
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
html_doc = readFromFile('tt.html')
'''

for index,row in config.iterrows():
    print("Fetching Information for "+row['url'])
    
    html_doc = getPageSrc(row['url'])
    soup = BeautifulSoup(html_doc, 'html.parser')
    findallLinks(soup, row)
    
exit(0)   
#findallLinks (soup, "a", "id", "jdUrl", "0")
#print(config['url'][0])
#findallLinks (soup)
#findallLinks(soup, "a", "class", "js-asset-link", 0)
#findallLinks(soup, "a", "itemprop", "name codeRepository", 0)



      
