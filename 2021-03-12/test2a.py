# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:30:45 2021

@author: user
"""

def my_xor(msg,key):
    m_size = len(msg)
    k_size = len(key)
    
    ans = bytearray()
    for i in range(m_size):
        ans.append(msg[i]^key[i%k_size])

    return ans

def main():
    msg = 'Hello World!'
    key = 'Bye'
    
    msg_en = my_xor(msg.encode(),key.encode())
    msg_de = my_xor(msg_en,key.encode())
    
    print(msg_en)
    print(msg_de)
    
main()
    