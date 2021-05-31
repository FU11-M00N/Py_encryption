import tools
import my1 as mydes

def encrypt_file(file_name,key,iv):
    fr= open(file_name,'rb')
    fw= open(file_name+'.enc','wb')

    BSIZE= 8 
    data= fr.read(BSIZE)
    while(data):
        data_enc=mydes.encrypt_des(data,key,iv)
        fw.write(data_enc)
        data = fr.read(BSIZE)
    fr.close()
    fw.close()
def decrypt_file(file_name,key,iv):
    fr= open(file_name,'rb')
    fw= open(file_name+'.dnc','wb')

    BSIZE= 8+8
    data= fr.read(BSIZE)
    while(data):
        data_dec = mydes.decrypt_des(data,key,iv)
        fw.write(data_dec)
        data = fr.read(BSIZE)
    fr.close()
    fw.close()

def main():
    file_name = 'demo.txt'
    key = 'haha good'
    iv ='how are you'

    encrypt_file(file_name, key.encode() ,iv.encode())

    decrypt_file(file_name+'.enc', key.encode(),iv.encode())
    h1=tools.get_hash_file(file_name)
    h2=tools.get_hash_file(file_name+'.enc.dnc')

    if(h1==h2):
        print("same")
    else:
        print("not same")
main()