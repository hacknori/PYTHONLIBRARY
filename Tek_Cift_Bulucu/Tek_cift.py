# -*- coding: utf-8 -*-
"""
@author: Hacknori
"""
def main():
    num = int(input("Bir Sayı Giriniz: "))
    if (num % 2) == 0:
       print("{0} Çift Sayıdır.".format(num))
       main()
    else:
       print("{0} Tek Sayıdır.".format(num))
       main()
main()