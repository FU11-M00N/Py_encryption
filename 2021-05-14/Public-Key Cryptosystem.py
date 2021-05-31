# -*- coding: utf-8 -*-
"""
Created on Fri May 14 09:10:32 2021

@author: user
"""

import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
MY_PR_KEY = 'pr_mhj.key'
MY_PU_KEY = 'pu_mhj.key'
# =============================================================================
#   키 관리
# =============================================================================

def make_key(pr_path, pu_path,size_bit=1024):
    pr_key = RSA.generate(size_bit)
    pu_key = pr_key.publickey()
    
    fw = open(pr_path,'wb')
    fw.write(pr_key.exportKey('PEM'))
    
    fw.close()
    fw = open(pu_path,'wb')
    fw.write(pu_key.exportKey('PEM'))
    
    fw.close()

def get_key(key_path):
    fr = open(key_path,'rb')
    key = RSA.importKey(fr.read())
    fr.close()
    
    return key
    
make_key(MY_PR_KEY,MY_PU_KEY)

# =============================================================================
#   메시지 암호화
# =============================================================================
    
    
def enc_msg(msg,key):
    ch = PKCS1_OAEP.new(key)
    enc_msg = ch.encrypt(msg)
    
    return enc_msg

def dec_msg(msg, key):
    ch = PKCS1_OAEP.new(key)
    dec_msg = ch.decrypt(msg)
    
    return dec_msg


def test1():
    msg = 'I LIKE PYTHON~!'
    
    pu_key = get_key(MY_PU_KEY)
    
    e_msg = enc_msg(msg.encode(), pu_key)
    
    print(e_msg)
    print(len(e_msg))
    
    pr_key = get_key(MY_PR_KEY)
    
    d_msg = dec_msg(e_msg,pr_key)
    
    print(d_msg)



def test1a():
    msg = 'hihihi'
    pu_key = get_key('ub_pu.key')
    
    e_msg = enc_msg(msg.encode(), pu_key)
    e_msg_txt = base64.b64encode(e_msg)
    print(e_msg_txt)
    

def test1b():
    e_msg_txt = 'Lx4EI1kvX4IThTAm9KCAF+cOE+sJf7O1A4DILJwyp0POBi9wuEAAgdoLQzhzfSk2NGPA195iYsjou9ilVIikABsmQJ4+3E7aapjCdQIQM1UD+UsPTh/IPiGpXYyxJ/bkCUpY5N/XSGREYMp4bMYRQX30jjnI9W2NDolqSdAs0NU='
    
    e_msg = base64.b64decode(e_msg_txt)
    
    pr_key = get_key(MY_PR_KEY)
    
    d_msg = dec_msg(e_msg,pr_key)
    
    print(d_msg)

#test1()
#test1a()
#test1b()


# =============================================================================
#   파일 암복호화
# =============================================================================

def encrpt_file(file_name,save_name,key):
    fw = open(save_name,'wb')
    fr = open(file_name,'rb')

    B_SIZE = 86
    data = fr.read(B_SIZE)
    
    while(data):
        data_enc= enc_msg(data,key)
        fw.write(data_enc)
        data = fr.read(B_SIZE)
    fw.close()
    fr.close()

def get_hash_file(file_name):
    fh = open(file_name,'rb')
    # sha = Hash.SHA256.new()
    sha = SHA256.new()
    

    
    data=fh.read(1024*2)
    while data:
        sha.update(data)
        data = fh.read(1024*2)
        
    hv = sha.digest()
    
    return hv

def decrpt_file(file_name,save_file, key):
    fw=open(save_file,'wb')
    fr=open(file_name,'rb')
    
    B_SIZE = 128 
    data = fr.read(B_SIZE)
    while data:
        data_dec = dec_msg(data,key)
        fw.write(data_dec)
        data = fr.read(B_SIZE)

    fw.close()
    fr.close()


def test2():
    file_name = 'test.py'
    file_save = file_name+'.enc'
    
    pu_key = get_key(MY_PU_KEY)
    encrpt_file(file_name,file_save,pu_key)
    
    txt_file= file_name+'.dec'
    pr_key = get_key(MY_PR_KEY)
    decrpt_file(file_save,txt_file,pr_key )

    h1 = get_hash_file(file_name)
    h2 = get_hash_file(txt_file)

    if h1==h2:
        print("same")
    else:
        print("not same")
test2()







    

