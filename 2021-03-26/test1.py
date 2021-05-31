# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 10:12:48 2021

@author: user
"""
from Crypto.Hash import SHA512
import base64

def get_hash(msg):
    sha = SHA512.new()
    sha.update(msg)
    hv = sha.digest()
    
    return hv

def main():
    msg = 'I Love *Python*'
    hv = get_hash(msg.encode())
    
    hv_txt = base64.b64encode(hv)
    hv_txt_bin = base64.b64decode(hv_txt)
    
    if hv == hv_txt_bin:
        print('Same')
    else:
        print('Not Same')
    
    
    print('hv :' , hv)
    print('hv_txt :' , hv_txt)
    print('hv_txt_bin :' , hv_txt_bin)

main()