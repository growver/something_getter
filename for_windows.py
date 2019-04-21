#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 00:34:16 2019

@author: joil
"""

import cv2
import os
def color_changer(sourcedir,exitdir):
    f=os.listdir(sourcedir)
    f=[f for a in f if ".jpg" in a]
    for path in f:
    	img = cv2.imread(sourcedir+"//"+path)
    	img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    	cv2.imwrite(exitdir+"//"+path)
