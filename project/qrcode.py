# -*- coding: utf-8 -*-
"""
Created on Tue May 26 12:49:19 2020
install pypng,pyzbar,pyqrcode


@author: hj823
"""

import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image
qr = pyqrcode.create("Audi_R8_2017")
qr.png("Audi_R8_2017.png", scale=6)
decode(Image.open('Audi_R8_2017.png'))
print(qr.data)


