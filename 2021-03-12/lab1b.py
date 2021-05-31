# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:47:14 2021

@author: user
"""

def encrypt_reverse(msg):
    
    size = len(msg)
    
# =============================================================================
#   크기 지정 x
# =============================================================================
    # ans = bytearray()
    
    # for i in range(size):
    #     a = msg[size-1-i]
    #     ans.append(a)
    
    
# =============================================================================
#     크기 지정 o
# =============================================================================
    
    ans = bytearray(size)
    
    for i in range(size):
        a=msg[size-1-i]
        ans[i] = a

    return ans

def main():
    msg = 'i love you'
    
    msg_enc = encrypt_reverse(msg.encode())
    msg_dec = encrypt_reverse(msg_enc)
    
    print(msg)
    print(msg_enc)
    print(msg_dec)
    
    print(msg_dec.decode())
main()