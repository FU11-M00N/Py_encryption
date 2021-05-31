# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 09:07:36 2021

@author: user
"""

from Crypto.Hash import SHA256
import base64

def get_hash(msg):
    
    sha = SHA256.new()

    sha.update(msg)

    hv = sha.digest()

    return hv


def get_hash_file(file_name):
    
    fh = open(file_name) # read, byte
    sha = SHA256.new()
    data = fh.read(100)
    sha.update(data)

    while data:
          
        data = fh.read(100)
        sha.update(data)
    
    hv = sha.digest()
    
    return hv
    
    
#def main():
    
 #   file_name = 'test2.py'
  #  hv = get_hash_file(file_name)
   # hv_txt = base64.b64encode(hv)
    
   # print(hv)
   # print(hv_txt)
    
    

#main()