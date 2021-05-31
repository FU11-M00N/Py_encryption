# -*- coding: utf-8 -*-
"""
Created on Fri May  7 10:46:37 2021

@author: user
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# =============================================================================
# 키 생성
# =============================================================================

def make_key():
    pr_key = RSA.generate(2048)
    pu_key = pr_key.publickey()
    
    print(pr_key)
    
    fw = open('prkey.pem','wb')
    fw.write(pr_key.exportKey('PEM'))

    
    fw = open('pukey.pem','wb')
    fw.write(pu_key.exportKey('PEM'))
    fw.close()

# make_key()
# =============================================================================
# 키 파일 가져오기
# =============================================================================

def load_key(path):
    fr = open(path,'rb')
    key = RSA.import_key(fr.read())
    return key
    
# =============================================================================
# 메시지 암복호화
# =============================================================================

def encrypt_msg(msg, key):
    cipher = PKCS1_OAEP.new(key)
    msg_enc = cipher.encrypt(msg)
    
    return msg_enc

def decrypt_msg(msg,key):
    cipher = PKCS1_OAEP.new(key)
    r_msg = cipher.decrypt(msg)
    
    return r_msg

# =============================================================================
# 테스트
# =============================================================================

def test1():
    make_key()
    pr_key = load_key('prkey.pem')
    pu_key = load_key('pukey.pem')

    msg = 'I hate unbi'
    msg_enc = encrypt_msg(msg.encode(), pu_key)
    print(msg)
    print(msg_enc)
    print(len(msg_enc))
    msg_enc_txt = base64.b64encode(msg_enc)
    print("----",msg_enc_txt)
    r_msg_enc = base64.b64decode(msg_enc_txt)
    r_msg = decrypt_msg(r_msg_enc,pr_key)
    
    print(r_msg)
    
# test1()

def test2():
    fr = open('unbimsg.txt', 'rb')
    r_msg = fr.read()
    r_msg = base64.b64decode(r_msg)
    pr_key = load_key('unbipr.pem')
    r_msg = decrypt_msg(r_msg,pr_key)
    print(r_msg)
test2()














