# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:12:39 2021

@author: user
"""

import tools
from Crypto.Cipher import DES3

def add_padd(msg):
    pad_len = 8 - len(msg) % 8
    pad = chr(pad_len)*pad_len
    
    return msg + pad.encode()

def remove_padd(msg):
    pad_len = msg[-1]
    
    return msg[:-pad_len]

def test1():
    msg = '012345674'
    msg_padd = add_padd(msg.encode())
    msg_rpad = remove_padd(msg_padd)
    
    print(msg)
    print(msg_padd)
    print(msg_rpad)

# test1()

# =============================================================================
# key 값을 hash 로 ~
# =============================================================================
def get_hash_key(key):
    key_h = tools.get_hash(key)
    
    return key_h[:24]

# =============================================================================
# iv 값을 hash 로~
# =============================================================================
def get_hash_iv(iv):
    iv_h = tools.get_hash(iv)
    return iv_h[:8]

# =============================================================================
# 암호화 하기
# =============================================================================
def encrypt_des(msg,key,iv):
    key_h = get_hash_key(key)
    iv_h = get_hash_iv(iv)
    msg_padd = add_padd(msg)
    des = DES3.new(key_h,DES3.MODE_CBC, iv_h)
    msg_enc = des.encrypt(msg_padd)
    
    return msg_enc

# =============================================================================
#  복호화 하기
# =============================================================================
def decrypt_des(msg,key,iv):
    key_h = get_hash_key(key)
    iv_h = get_hash_iv(iv)
    des = DES3.new(key_h,DES3.MODE_CBC, iv_h)
    msg_dec = des.decrypt(msg)
    msg_rpad = remove_padd(msg_dec)
    
    return msg_rpad

# =============================================================================
# 3DES test
# =============================================================================
def main():
    # DES의 msg는 8의배수로 나타나야함.
    # KEY 는 24바이트가 되어야함.
    msg = 'I Like Python~!' # msg 8바이트
    key = 'hisecure' # KEY 24바이트
    iv = '01234567' # iv 8바이트
    
    msg_enc = encrypt_des(msg.encode(),key.encode(),iv.encode())
    msg_enc_des = decrypt_des(msg_enc,key.encode(),iv.encode())
    
    print(msg)
    print(msg_enc)
    print(msg_enc_des)

#main()