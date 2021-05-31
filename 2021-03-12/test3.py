def my_xor(msg,key):
    p_size = len(msg)
    k_size = len(key)
    ans= bytearray()

    for i in range(p_size):
        ans.append( msg[i] ^ key[i%k_size])

    return ans
        


def main():
    msg= 'moonhojun'
    key= 'goo'
    
    msg_en = my_xor(msg.encode(),key.encode())
    msg_de = my_xor(msg_en,key.encode())
    
    print (msg_en)
    print (msg_de)