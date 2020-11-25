# -*- coding: utf-8 -*-
"""
@author: Hacknori
"""
print("Hacknori'nin En Büyük Tek Sayı Bulucusuna Hoşgeldiniz.")
liste=[]
i=0
while i<10:
    sayi=int(input(str(i+1)+". sayıyı girin: "))
    liste=liste+[sayi]
    i+=1
    
print(liste)
a=0
liste[0]=a
for n in liste:
    if(not(n%2==0)):
        if(n>a):
            a=n
            
if(not(a%2==0)):            
    print("En büyük tek sayı: "+str(a))
else:
    print("Tek sayı yok!")
        
            