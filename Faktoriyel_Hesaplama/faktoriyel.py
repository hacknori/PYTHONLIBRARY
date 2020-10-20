# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:52:17 2020

@author: Hacknori
"""

sayi = int(input("Faktöriyel hesaplamak için sayı girin:"))
faktoriyel = 1
for i in range(sayi):
    faktoriyel = faktoriyel * (i+1)
    
 
print("Faktoriyel : ", faktoriyel)