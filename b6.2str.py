# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:22:37 2024

@author: lebaottran
"""
chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"

phan1, phan2, phan3, phan4, phan5 = chuoi.split(", ")

phan3 = phan3.replace("P. ", "")
phan4 = phan4.replace("Q. ", "")
phan5 = phan5.replace("Tp. ", "")

sub_strings = [phan1, phan2, phan3, phan4, phan5]
for s in sub_strings:
    print(s)
