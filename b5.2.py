# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:27:28 2024

@author: lebaotran

"""

a = int(input("nhap so nguyen a:"))
b = int(input("nhap so nguyen b:"))

tong = a + b
hieu = a - b
tich = a * b
thuong = round(a / b, 3)
chialaydu = a % b
chialaynguyen = a // b
print("Tổng: ",tong)
print("Hiệu:", hieu)
print("Tích: ",tich)
print("Thương (làm tròn 3 chữ số): ",thuong)
print("Chia lấy dư:",chialaydu)
print("Chia lấy nguyên:", chialaynguyen)
