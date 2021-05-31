# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:21:03 2021

@author: user
"""

# B_SIZE 몇바이트면 몇바이트?

import tools
import DES_lib as mydes

def encrypt_file(file_name,key,iv):
    fr = open(file_name,'rb')
    fw = open(file_name+'.enc','wb')
    
    B_SIZE = 8
    
    data = fr.read(B_SIZE)
    while data:
        data_enc = mydes.encrypt_des(data,key,iv)
        fw.write(data_enc)
        
        data =fr.read(B_SIZE)
    
    fr.close()
    fw.close()
    

def decrypt_file(file_name,key,iv):
    fr = open(file_name,'rb')
    fw = open(file_name+'.dec','wb')
    
    B_SIZE = 8 + 8
    #B_SIZE = 원래 encrypt size //8 + 1
    
    data = fr.read(B_SIZE)
    
    while data:
        data_enc = mydes.decrypt_des(data,key,iv)
        fw.write(data_enc)
        
        data =fr.read(B_SIZE)
    
    fr.close()
    fw.close()

def main():
    file_name='demo.txt'
    key = 'What Do You Want?'
    iv = 'I Want to learn Python'
    
    encrypt_file(file_name,key.encode(),iv.encode())
    decrypt_file(file_name+'.enc',key.encode(),iv.encode())

    h_org = tools.get_hash_file(file_name)
    h_dec = tools.get_hash_file(file_name+'.enc.dec')
    
    if h_org==h_dec:
        print('Same')
    else:
        print('Not Same')

main()