from Crypto.Hash import SHA512
import base64
  
def file_copy():
   
    fh= open('hoho.txt','rb')

    data=fh.read(100)
    
    sha=SHA512.new()
    sha.update(data)


    while data:
        data = fh.read(100)
        sha.update(data)
    
    
    hv=sha.digest()
    base_hv =base64.b64encode(hv)

    return base_hv

   

def get_hash(msg):
    sha= SHA512.new()
    sha.update(msg)
    hv = sha.digest()

    return hv

def main():
    
    message= "i like python"
    ub2= "Jsup6Kci91O56/jJ4Le0XBQmcfUeahTCNpFAuWSTXUwhmJOKFESv0fJzHB26FvlkNds5Mi+aRTtod/Zw9G7a1Q=="
    ub_decode=base64.b64decode(ub2)
    hv = get_hash(message.encode())
    hv_base =base64.b64encode(hv)
    print(hv)
    print("----------------------------------------------------")
    print(hv_base)

    if ub2 == ub_decode:
        print("같음")
    else:
        print("다름")
    print(file_copy())
    

main()

   

















