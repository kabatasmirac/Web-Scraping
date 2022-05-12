#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:38:40 2020

@author: mirac
"""
import excel_reader as exr
import urllib.request, json 

with urllib.request.urlopen("https://api.trendyol.com/sapigw-product/product-categories") as url:
    data = json.loads(url.read().decode())
    
global cat_list
cat_list=[]
kat=[]
def get_cat(cat,cat_list,kat):
    attr_list=[]
    
    cat_list.insert(len(cat_list),cat.get('name'))
    
    for x in cat.get('subCategories'):                   
        get_cat(x, cat_list,kat)
    
    if len(cat.get('subCategories')) == False:
        with urllib.request.urlopen("https://api.trendyol.com/sapigw/product-categories/"+str(cat.get('id'))+"/attributes") as url_2:
            try :
                altozellik = json.loads(url_2.read().decode())
                for x in altozellik.get('categoryAttributes'):                
                    attr_list.insert(len(attr_list),(x.get('attribute')).get('name'))
            except Exception as e:
                print(e)
                
    cat_list.insert(len(cat_list),attr_list)
    exr.addsheet(cat_list,kat)
    
    if cat_list[0] not in kat:
        kat.append(cat_list[0])
    
        
    del cat_list[1:]    
    
for i in data.get("categories"):
    
   
    print(i.get('name'))
    get_cat(i,cat_list,kat)
    cat_list.clear()