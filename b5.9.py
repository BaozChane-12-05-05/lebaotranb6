# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:14:19 2024

@author: lebaotran
"""
a = float(input("Nhập số thực a: "))
b = float(input("Nhập số thực b: "))
A = ((a**0.5-b**0.5)/(a**0.25-b**0.25))-((a**0.5+(a*b)**0.25)/(a**0.25+b**0.25))
print("kết quả là" , A)