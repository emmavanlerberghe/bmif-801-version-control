#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 11:42:01 2018

@author: emmavanlerberghe
"""


s=(input('please enter string: '))
s2 = s.strip('?,.\'\"!:')
#b = "?,.\'\"!:" 
#for char in b:
    #s = s.replace(char,"") 
print(s2) 
mylist=s2.split() 
#s.strip() 
print(mylist) 
print(len(mylist)) 

for item in mylist :
    print('individual words are:  %s '% item)  
    
#havent done count yet but that is for the future 
    
 
