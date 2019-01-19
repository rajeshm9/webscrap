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


url="https://www.naukri.com/devops-jobs"
url="https://www.usatoday.com/"
url="https://github.com/rajeshm9?tab=repositories"
'''
VERSION BUILD=1005 RECORDER=CR
URL GOTO=https://www.naukri.com/devops-jobs
TAB OPEN
TAG POS=1 TYPE=A ATTR=ID:jdUrl
TAG POS=1 TYPE=BUTTON ATTR=TXT:Next


'''
options = Options()
#options.set_headless(headless=True)
#options.add_argument("--headless")
    
def getPageSrc (url):
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)
    
    src =  driver.page_source
    driver.close()
    return src



def findallLinks(soup, link, next):
    
    for a in soup.find_all(link['type'] , {link['attr']:}):
        print(a.get('href'))
        
    
html_doc = getPageSrc(url)
soup = BeautifulSoup(html_doc, 'html.parser')

link['type'] = 'a'
link['attr'] = 'id'
link['val'] ='jdUrl'
#findallLinks (soup, "a", "id", "jdUrl", "0")
findallLinks (soup, "a", "id", "jdUrl", "0")
#findallLinks(soup, "a", "class", "js-asset-link", 0)
#findallLinks(soup, "a", "itemprop", "name codeRepository", 0)



      
