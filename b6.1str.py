# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:06:30 2024

@author: lebaotran
"""

chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
sub_strings = [s.strip() for s in chuoi.split(",")]
for s in sub_strings:
    print(s)
