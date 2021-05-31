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


def main():
    
    msg = "I love python"
    hv = get_hash(msg.encode())
    
    print(len(hv))
    
    print(hv)
    
    msg1 = "I love python"
    
    hv1 = get_hash(msg1.encode())
    
    print(hv1)
    
    if hv == hv1:
        print('Same')
    else: 
        print('Not Same')
        
    hv1_txt = base64.b64encode(hv1)
    hv1_txt_bin = base64.b64decode(hv1_txt)
    
    print(hv1_txt)
    print(hv1_txt_bin)
    
    if hv1 == hv1_txt_bin:
        print('Same')
    else:
        print('Not Same')
    
    
    

main()