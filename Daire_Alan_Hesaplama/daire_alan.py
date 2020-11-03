# -*- coding: utf-8 -*-
"""
@author: Hacknori
"""
#Pi değerimizi tanımlıyoruz.
pi = 3.14159

#Kullanıcıdan yarıçapı alıyoruz
ycap=input("Dairenin yarıçapını giriniz:")

#Aldığımız değeri stringden int'e çeviriyoruz ki işlem yapabilelim
ycapint=int(cap)

#Alan hesaplama formülünü kullanarak dairenin alanını buluyoruz
alan=pi*(ycapint**2)

#Alanı yazdırıyoruz
print("Dairenin Alanı:",alan)

