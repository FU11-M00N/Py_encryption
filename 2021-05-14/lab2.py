# -*- coding: utf-8 -*-
"""
Created on Fri May 14 10:30:36 2021

@author: user
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import lab1 as my_tool


# =============================================================================
# 메세지 서명
# =============================================================================

def sign_msg(msg,key):
    h_obj = SHA256.new(msg)
    signer = PKCS1_v1_5.new(key)
    
    sign_value = signer.sign(h_obj)
    
    return sign_value

def verify_msg(msg,sign_value,key):
    h_obj = SHA256.new(msg)
    verifyer = PKCS1_v1_5.new(key)
    
    ans = False
    
    if verifyer.verify(h_obj,sign_value):
        ans = True
    
    return ans

def test1():
    msg = 'I LIKE PYTHON!'
    
    pr_key = my_tool.get_key('pr_mhj.key')
    pu_key = my_tool.get_key('pu_mhj.key')
    sign_value = sign_msg(msg.encode(),pr_key)
    
    print(sign_value)

    # sign_txt = base64.b64encode(sign)
    # print(sign_txt)
    
    if verify_msg(msg.encode(),sign_value,pu_key):
        print('문제 없음여!')
    else:
        print('문제가 생겼나봐요!')
        
def test1a():
    msg = 'And I LOVE PYTHON!'
    pr_key = my_tool.get_key('pr_mhj.key')
    
    sign_value = sign_msg(msg.encode(),pr_key)
    sign_value_txt = base64.b64encode(sign_value)
    
    print(msg)
    print(sign_value_txt)
    
def test1b():
    msg = 'And I LOVE PYTHON!'
    sign_value_txt = 'qffiJyH/2ABexidpdgGg1H3OSsjnuGdCDg/zNgEcIOUO6bzyGz3XMAD0vWRWUKtPeibjXWaiKv3vEipfvUmxXyNKfMpD4LNBf1x92eGWqwD6zLIMs4iV0D4fwx1kz9+dh0DkHwGgHu4ZXCcY83UvCCc/6HGOU3LMkrVAnZ6QbhM='
    
    pu_key = my_tool.get_key('pu_mhj.key')
    
    sign_value = base64.b64decode(sign_value_txt)
    if verify_msg(msg.encode(),sign_value,pu_key):
        print('정직해!')
    else:
        print('거짓말 치지마!')

# test1()
# test1a()
#test1b()

###################################################
# sign file
###################################################

def sign_file(file_name,key):
    fr = open(file_name, 'rb')
    
    data = fr.read()
    fr.close()
    hobj = SHA256.new(data)
    signer= PKCS1_v1_5.new(key)

    sign_value = signer.sign(hobj)
    
    return sign_value

def verify_file(file_name,sign_value, key):
    fr= open(file_name,'rb')

    data = fr.read()
    hobj= SHA256.new(data)

    verifyer= PKCS1_v1_5.new(key)
    if verifyer.verify(hobj,sign_value):
        return True
    else:
        return False
    

def test2():
    file_name = 'test.py'
    pr_key = my_tool.get_key('pr_mhj.key')
    sign_value = sign_file(file_name, pr_key)
    print(sign_value)

    pu_key = my_tool.get_key('pu_mhj.key')
    if verify_file(file_name , sign_value , pu_key):
        print("verify")
    else:
        print("not verify")
#test2()

def test2a():
    file_name = 'test.py'
    pr_key = my_tool.get_key('pr_mhj.key')
    sign_value = sign_file(file_name, pr_key)

    sign_value_txt = base64.b64encode(sign_value)
    print(sign_value_txt)

def test2b():
    file_name = 'test.py'
    sign_value_txt = 'OzBzCY3EbvE5u4uYCXdR17PEwl+kwk2JKKGFkaLoWrwjxU2EWuNd1/GvgSPx/Xx5OSsYn2RP9SP+sUqGwYWNzWw/bqO+FVdld5yLX7cJ84Ra+OQtfXlYidlZiDeHBXkrG0EAr1jlkzsmrMK7+aldgwg6/l1nXu8RLo/LeD5xNR0='
    pu_key = my_tool.get_key('pu_mhj.key')

    sign_value = base64.b64decode(sign_value_txt)
    if verify_file(file_name, sign_value, pu_key):
        print('verify')
    else:
        print('not verify ')
    
#test2a()
test2b()