#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:20:23 2020

@author: mirac
"""


import attr_cat_reader as attrcat
import urllib.request, json 


f= open("product_id.txt","r")
while 1:
    attr_list=[]
    line=f.readline()
    line=line.rstrip() 
    with urllib.request.urlopen(r"https://api.trendyol.com/sapigw/product-categories/"+line+"/attributes") as url_2:
        altozellik = json.loads(url_2.read().decode())
        attr_list.insert(len(attr_list),altozellik.get('name'))
        for i in range(0,len(altozellik.get('categoryAttributes'))):
            attr_list.insert(len(attr_list),altozellik.get('categoryAttributes')[i].get('attribute').get('name'))
            for j in range(0,len(altozellik.get('categoryAttributes')[i].get('attributeValues'))):
                attr_list.insert(len(attr_list),altozellik.get('categoryAttributes')[i].get('attributeValues')[j].get('name'))
                attrcat.addsheet(attr_list)
                attr_list.pop()
            attr_list.pop()      
        attr_list.pop()
        print("bitti")
    
