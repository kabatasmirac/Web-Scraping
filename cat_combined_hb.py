#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 16:20:54 2020

@author: mirac
"""


import pandas as pd
import numpy as np
data = pd.read_excel("opt_attr.xlsx")
attr_list=pd.DataFrame(columns=['Kategori','Özellik Adı','Özellik Seçenekleri'])
controller = []
for i in range(0,data.shape[0]):
    em_row={'Kategori':'nan','Özellik Adı':'nan','Özellik Seçenekleri':'nan'}
    attr_list=attr_list.append(em_row,ignore_index=True)
    attr_list.iloc[i,0]=(data._get_value(i,'Kategori'))
    attr_list1=[]
    if [data._get_value(i,'Kategori'),data._get_value(i,'Özellik Adı')] not in controller:
        controller.append([data._get_value(i,'Kategori'),data._get_value(i,'Özellik Adı')])
        
        
        for j in range(i,data.shape[0]):
            
            attr_list.iloc[i,1]=(data._get_value(i,'Özellik Adı'))
            
            
            if data._get_value(i,'Kategori')==data._get_value(j,'Kategori') and data._get_value(i,'Özellik Adı')==data._get_value(j,'Özellik Adı'):
                attr_list1.append(data._get_value(j,'Özellik Seçenekleri'))
                print(data._get_value(j,'Özellik Seçenekleri'))
        
    print("***************************************")
    print(attr_list1)
    attr_list.iloc[i,2]=(attr_list1)
attr_list.to_excel("attr_list.xlsx")    