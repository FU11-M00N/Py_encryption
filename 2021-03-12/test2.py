# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 11:23:32 2021

@author: user
"""

def my_re(msg):
    msg_size = len(msg)
    ans = bytearray()
    
    for i in range (msg_size):
        ans.append(msg[msg_size-1-i])
    
    return ans
        
def main():
    msg = 'i love you'
    
    msg_en = my_re(msg.encode())
    msg_de = my_re(msg_en)
    
    print(msg_en)
    print(msg_de)

    
main()