# -*- coding: utf-8 -*-
"""
@author: Hacknori
"""
#Pi değerimizi tanımlıyoruz.
pi = 3.14159

#Kullanıcıdan yarıçapı alıyoruz
ycap=input("Dairenin yarıçapını giriniz:")

#Aldığımız değeri stringden float'a çeviriyoruz ki işlem yapabilelim
ycapf=float(ycap)

#Alan hesaplama formülünü kullanarak dairenin alanını buluyoruz
alan=pi*(ycapf**2)

#Alanı yazdırıyoruz
print("Dairenin Alanı:",alan)

