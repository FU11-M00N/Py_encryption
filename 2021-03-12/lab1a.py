# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:11:24 2021

@author: user
"""


# =============================================================================
# reverse 암호화
# =============================================================================
def encrypt_re(msg):
    s=''
    for i in range(0,len(msg)):
        s+=msg[len(msg)-1-i]
    
    return s


def main():
    msg = 'i love you'
    
    msg_enc = encrypt_re(msg)
    print(msg_enc)

    msg_dec = encrypt_re(msg_enc)
    print(msg_dec)
    
    
main()

