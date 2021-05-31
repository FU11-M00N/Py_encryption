
# 1> python 소스 파일 (소스파일, 실험파일(메시지 암복호화, 파일 암복호화)

def msg_enc(msg,s):
    i=0
    j=0
    stream_key= []
    msg=msg.encode()
    enc_value=bytearray()
    
    for k in range(len(msg)):
        i=(i+1) % 256
        j=(j+s[i]) % 256
        s[i],s[j]=s[j],s[i]
        stream_key.append(s[(s[i] + s[j])%256])
        enc_value.append( msg[k] ^ stream_key[k])
    return enc_value

def msg_dec(enc_value,s):
    i=0
    j=0
    stream_key= []
    dec_value=bytearray()

    for k in range(len(enc_value)):
        i=(i+1) % 256
        j=(j+s[i]) % 256
        s[i],s[j]=s[j],s[i]
      
        stream_key.append(s[(s[i] + s[j])%256])
        dec_value.append(enc_value[k] ^ stream_key[k])
    return dec_value

def key_init(key): # 섞인 s 생성 
    key = key.encode()
    j=0
    s= []
    for i in range(0,256):
        s.append(i)
    for i in range(0,256):
        
        j=(j + s[i] + key[i%len(key)]) %256
        s[i],s[j] = s[j],s[i]        
    return s

def main():
    print("파일 이름 입력")
    file_name = input()
    fh = open(file_name,'r') # read, byte

    value = fh.read()

    print("키 입력")
    key=input()

    s=key_init(key)

    
    enc_value=msg_enc(value,s)
    print("암호화 값 : ",enc_value)
    
    dec_value=msg_dec(enc_value,key_init(key))
    print("복호화 값 : ", dec_value)
   
    


main()