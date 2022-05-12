#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:21:54 2020

@author: mirac
"""
import json 
import excel_reader_hb as exr
import os


global cat_list,attr_list
cat_list=[]
kat=[]

attr_list=[]
def get_cat(cat,cat_list,kat,attr_list):
    
    
    if cat.get('KategoriList') is None:
        attr_list.insert(len(attr_list),cat.get('KategoriAdi'))
        
    else:
        cat_list.insert(len(cat_list),cat.get('KategoriAdi'))

        for x in cat.get('KategoriList'):  
              
            get_cat(x, cat_list,kat,attr_list)
            
          
    
        cat_list.insert(len(cat_list),attr_list)
        print(cat_list)
        exr.addsheet(cat_list,kat)
        for cat in cat_list:
            if cat not in kat and type(cat) != []:
                kat.append(cat)
            
        attr_list.clear()    
        cat_list.pop()
        cat_list.pop()
#for x in os.listdir('hb_kategoriler/'):
# Opening JSON file 
with open('hb_kategoriler/elekt.json',encoding="cp866") as url:

    data = json.load(url)
    
for i in data.get("categories"):
    
   
    print(i.get("KategoriAdi"))
    get_cat(i,cat_list,kat,attr_list)
    cat_list.clear()