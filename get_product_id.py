#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 01:05:37 2020

@author: mirac
"""

import urllib.request, json 

with urllib.request.urlopen("https://api.trendyol.com/sapigw-product/product-categories") as url:
    data = json.loads(url.read().decode())
    
global cat_list
cat_list=[]
f=open("product_id.txt","a+")
def get_cat(cat,cat_list):
    attr_list=[]
    cat_list.insert(len(cat_list),cat.get('name'))
    
    for x in cat.get('subCategories'):                   
        get_cat(x, cat_list)
    
    if len(cat.get('subCategories')) == False:
        f.writelines(str(cat.get('id'))+"\n")
        
                
    cat_list.insert(len(cat_list),attr_list)
    del cat_list[1:]    
    
for i in data.get("categories"):
    
    get_cat(i,cat_list)
    cat_list.clear()
    