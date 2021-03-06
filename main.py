#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:51:39 2019

@author: joil
"""


import bs4
from lxml import html
import requests
from time import sleep
import datetime
import os


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
            #text=text.replace("iphone", "android")
            
            
            #URLが載っていない要素は何も返さないのでここで捨てる.
            if len(text)==0:
                pass
            else:
                result.append(text)
                
    #なぜかわからんけど同じ要素がたくさん出現してくどいから消す.
    return list(set(result))

def saver(URL,savedir):
    l=getter(URL)
    f=os.listdir(savedir)
    f=[a for a in f if ".jpg" in a]
    for var in range(0,len(l)):
        try:
            download_img(l[var], savedir+"//"+str(var+len(f))+".jpg")
            sleep(1)
        except:
            pass
        