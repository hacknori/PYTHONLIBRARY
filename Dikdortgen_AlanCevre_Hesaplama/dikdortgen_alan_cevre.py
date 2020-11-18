# -*- coding: utf-8 -*-
"""
@author: Hacknori

"""
def main():
    k=input("Kısa kenarı giriniz: ")
    u=input("Uzun kenarı giriniz: ")
    a=int(k)*int(u)
    c=(int(k)+int(u))*2
    print("Alan: "+str(a))
    print("Çevre: "+str(c))
    main()
main()