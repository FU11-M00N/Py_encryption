# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:03:37 2021

@author: user
"""

def crypt_xor(msg,key):
    m_size=len(msg)
    k_size = len(key)
    ans = bytearray()
    
    for i in range(m_size): 
        m = msg[i]
        
        # k = key[i % k_size]
        k = key[i-k_size] # 파이썬은 -index 가 가능하다
        
        a=m^k
        ans.append(a)
                   
    return ans
    
def main():
    msg = 'i love you'
    key = 'hisecure'
    
    msg_enc = crypt_xor(msg.encode(),key.encode())
    msg_dec = crypt_xor(msg_enc,key.encode())
    
    print(msg)
    print(msg_enc)
    print(msg_dec)
    print(msg_dec.decode())
    
main()