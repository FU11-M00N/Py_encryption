# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 10:45:21 2021

@author: user
"""
def my_enc(msg,key):
    
    msg = msg.lower()
    ans = bytearray()
    
    for m in msg:
        if(ord('a') <= m <= ord('z')):
            index = m - ord('a')
            index = index + key
            index = index % 26
            
            ans.append(index+ ord('a'))
            
        else:
            ans.append(m)
        
    return ans

def my_dec(msg,key):

    ans = bytearray()
    
    for m in msg:
        if(ord('a') <= m <= ord('z')):
            index = m - ord('a')
            index = index - key
            index = index % 26
            
            ans.append(index + ord('a'))
            
        else:
            ans.append(m)
        
    return ans

def main():
    msg = 'i love you Zz~!'
    key = 2
    
    msg_enc = my_enc(msg.encode(),key)
    msg_dec = my_dec(msg_enc,key)
    
    print(msg)
    print(msg_enc)
    print(msg_dec)

main()