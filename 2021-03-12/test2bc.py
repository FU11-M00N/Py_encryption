# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:37:04 2021

@author: user
"""

def my_enc_xor(msg, key):
    m_size = len(msg)
    k_size = len(key)
    
    ans = bytearray()
    
    for i in range(m_size):
        ans.append(msg[i]^key[i%k_size])
        
    return ans

def main():
    msg = 'Hello World!'
    key = 'bye'
    
    msg_enc= my_enc_xor(msg.encode(),key.encode())
    msg_dec = my_enc_xor(msg_enc, key.encode())
    
    print(msg_enc)
    print(msg_dec)
main()