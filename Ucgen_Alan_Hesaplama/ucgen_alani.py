# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:31:31 2020

@author: Hacknori
"""

def main():
    import math
    #(Henüz Çalışmıyor)4)Dik üçgenin dik kenarlarını biliyorsanız\n(Henüz Çalışmıyor)5)Çevrel çemberin yarıçapını ve kenar uzunluklarını biliyorsanız\n(Henüz Çalışmıyor)6)İç teğet çemberin yarıçapını ve üçgenin kenar uzunluklarını biliyorsanız
    print("Hacknori'nin üçgen hesaplayıcısına hoşgeldiniz.\nAşağıda bulunan seçeneklerden birini seçin.\n1)Taban uzunluğunu(yüksekliğin dik indiği kenarı) ve yüksekliği biliyorsanız\n2)İki kenar ve belirtmediğiniz kenarın açısını biliyorsanız\n3)Eşkenar üçgenin kenar uzunluğunu biliyorsanız\n")
    secim=input("Seçim yapınız:")
    
    if secim=="1":
        taban=float(input("Taban uzunluğu girin:"))
        yukseklik=float(input("Yükseklik girin:"))
        alan=(taban*yukseklik)/2
        print("Alan:"+str(alan))
        main()
        
    elif secim=="2":
        a=float(input("Kenar uzunluğunu girin:"))
        b=float(input("Diğer kenar uzunluğunu girin:"))
        aci=int(input("Vermediğiniz kenara ait açıyı girin:"))
        alan=(1/2)*a*b*(math.sin(math.radians(aci)))
        print("Alan:"+str(round(alan,1)))
        main()
    
    elif secim=="3":
        a=float(input("Kenar uzunluğunu girin:"))
        alan=(a*a*math.sqrt(3))/4
        print("Alan:"+str(alan))
        main()
    
    else:
        print("Hatalı seçim")
        main()
        
main()    