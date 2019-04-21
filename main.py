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
from time import sleep

def download_img(url, file_name):
    #画像をダウンローします.
    #クワシイコトハワカンナイ
    #curl的な何かだと思われる.
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(file_name, 'wb') as f:
            f.write(r.content)

def getter(url):
    #URLからURLを抜き出します
    
    #この辺ではページのHTMLソースを取得しています.
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    
    #URLが含まれているタグは<li>だったので,<li>の要素を全てelemsに入れます
    elems = soup.select('li')
    l=[]
    result=[]
    for elem in elems:
        #elemsの中には3通りのurlがある.
        #iPhone用　android用　なんかちっこいの
        #iphone用となんかちっこいのは画質とurlの末尾のみが異なる
        #なんかちっこいのは<div>タグで簡単に取得できる.
        l.append(str(elem.select('div')))
        for a in l:
            tex=a
            l2=[]
            
            #ターゲットURLは()でサンドイッチなので()の間の文字をリストに加える.
            for var in range(0,len(tex)):
                if tex[var]=="(":
                    var=var+1
                    while tex[var]!=")":
                        l2.append(tex[var])
                        var=var+1
                else:
                    pass
                
            #リストを文字列に直す
            text=""
            for x in l2:
                text += x
                
            #末尾をいじって なんかちっこいの=>iphone用 とする.
            text=text.replace("sticker_key@2x.png", "sticker@2x.png")
            
            #URLが載っていない要素は何も返さないのでここで捨てる.
            if len(text)==0:
                pass
            else:
                result.append(text)
                
    #なぜかわからんけど同じ要素がたくさん出現してくどいから消す.
    return list(set(result))

def saver(URL,savedir):
    l=getter(URL)
    for var in range(0,len(l)):
        download_img(l[var], savedir+"//"+str(var)+".jpg")
        sleep(1)
        




saver("https://store.line.me/stickershop/product/13758/ja","saver")