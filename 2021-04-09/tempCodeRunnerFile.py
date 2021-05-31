import tools
from Crypto.Cipher import DES3

def get_key(key):
    key_h= tools.get_hash(key)
    key_h= key_h[:24]

    return key_h

def get_iv(iv):
    iv_h= tools.get_hash(iv)
    iv_h= iv_h[:8]

    return iv_h

def encrypt_des(msg,key,iv):
    key_h=get_key(key)
    iv_h= get_iv(iv)


    des = DES3.new(key_h,DES3.MODE_CBC, iv_h)
    msg_enc = des.encrypt(msg)

    return msg_enc

def decrypt_des(msg,key,iv):
    key_h= get_key(key)
    iv_h = get_iv(iv)

    des = DES3.new(key_h,DES3.MODE_CBC, iv_h)
    msg_dec = des.encrypt(msg)
    return msg_dec

def main():
    msg = '01234567'
    key = 'i am good boy'
    iv = 'hisecure'

    msg_enc= encrypt_des(msg.encode(), key.encode(), iv.encode())
    msg_enc_dec= decrypt_des(msg.encode(),key.encode(),iv.encode())

    print("메세지 : ", msg)
    print("암호화 :", msg_enc)
    print("복호화 :", msg_enc_dec)
main()