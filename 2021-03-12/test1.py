# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 10:58:57 2021

@author: user
"""

def my(msg):
    
    size=len(msg)
    ans = bytearray()
    
    for i in range(size):
        a = msg[size-1-i]
        ans.append(a)

        
    return ans


def main():
    msg = 'hello world!'
    msg_enc = my(msg.encode())
    
    print(msg_enc)

main()