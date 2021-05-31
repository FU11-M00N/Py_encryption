# -*- coding: utf-8 -*-
import tools
from Crypto.Cipher import DES3
# ====================================================================
# 암호화 하기
# ====================================================================
def encrypt_des(msg,key,iv):
    des= DES3.new(key,DES3.MODE_CBC , iv ) # DES3.NEW 클래스, mode는 cbc모드
    msg_enc = des.encrypt(msg)

    return msg_enc    
# ====================================================================
# 복호화 하기
# ====================================================================
def decrypt_dex(msg,key,iv):
   des = DES3.new(key,DES3.MODE_CBC, iv)
   msg_dec = des.decrypt(msg)
   return msg_dec



# ====================================================================
# 3des test
# ====================================================================
def main(): 
    msg = '01234567' # DES3 암호일땐 msg는 8*n의 형태여야함.
    key = '012345678901234567890123' # DES3 일때 key는 24byte 이여야함.
    iv = '01234567' # DES3 일때 8바이트여야함. 

    msg_enc = encrypt_des(msg.encode(),key.encode(),iv.encode())
    msg_enc_dec = decrypt_dex(msg_enc, key.encode(), iv.encode())


    print("메세지 : ", msg)
    print("암호화 :", msg_enc)
    print("복호화 :", msg_enc_dec)
main()