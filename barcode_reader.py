#!/usr/bin/python3
# -*- coding: Utf-8 -*-

from __future__ import print_function
import pyzbar.pyzbar as pyzbar
import cv2
import urllib.request
import json
import pprint


def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # if you are interested in the debugging output you can print this for
    for obj in decodedObjects:
        # print('Type : ', obj.type)
        # print('Data : ', obj.data, '\n')
        pass

    return decodedObjects

# Read image
im = cv2.imread('location_to_image_of_bar_code')
api_key = "your_api_key"
url = 'https://api.barcodelookup.com/v2/products?barcode=' + decode(im)[0][0].decode(
    "utf-8") + '&formatted=y&key=' + api_key

print(url)
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

pprint.pprint(data)

# Main
if __name__ == '__main__':
    decodedObjects = decode(im)
    
