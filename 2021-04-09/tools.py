# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 17:10:52 2021

@author: clccclcc
"""

# =============================================================================
# >> conda install pycryptodome
# =============================================================================

# =============================================================================
# 
#  hash 와 base64에 대하여 이해 및 사용  binary_to_text 
#
# =============================================================================


# =============================================================================
# Hash tools 
# =============================================================================
# from Cryptodome.Hash  import SHA256
from Crypto.Hash import SHA256

import base64 


def get_hash(msg):
    sha = SHA256.new()
       
    # sha = Hash.SHA256.new()
    sha.update(msg)
    hv = sha.digest()
    
    return hv
    
def get_hash_file(file_name):
    fh = open(file_name,'rb')
    # sha = Hash.SHA256.new()
    sha = SHA256.new()
    

    
    data=fh.read(1024*2)
    while data:
        sha.update(data)
        data = fh.read(1024*2)
        
    hv = sha.digest()
    
    return hv
        

def main():
    msg='i love you'
    
    hv = get_hash(msg.encode())
    print(hv)
    
    hv_enc64= base64.b64encode(hv)
    print('b64_en:',hv_enc64)
    hv_dec64 = base64.b64decode(hv_enc64)
    print('b64_de:',hv_dec64)
    
    file_name='tools.py'
    hv = get_hash_file(file_name)
    print(hv)

# main()
 