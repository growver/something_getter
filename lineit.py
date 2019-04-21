#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:51:39 2019

@author: joil
"""

import selenium
import bs4
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request
from lxml import html
from urllib import request
import requests



url="https://store.line.me/stickershop/product/13758/ja"
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
elems = soup.select('li')
l=[]
result=[]
for elem in elems:
    l.append(str(elem.select('div')))
    for a in l:
        tex=a
        l2=[]
        for var in range(0,len(tex)):
            if tex[var]=="(":
                var=var+1
                while tex[var]!=")":
                    l2.append(tex[var])
                    var=var+1
            else:
                pass
        text=""
        for x in l2:
            text += x
        if len(text)==0:
            pass
        else:
            result.append(text)

l_unique = list(set(result))


