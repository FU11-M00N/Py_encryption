
def my_enc(msg,key):
    table=b'abcdefghijklmnopqrstuvwxyz0123456789'
    msg = msg.lower()
    ans= bytearray()
    
    for m in msg:
        index = table.find(m)
        if(index == -1):
            ans.append(m)
        else:
            index = index + key
            index = index % len(table)
            ans.append(table[index])
    return ans

def my_dec(msg,key):
    table=b'abcdefghijklmnopqrstuvwxyz0123456789'
    msg = msg.lower()
    ans= bytearray()
    for m in msg:
        index = table.find(m)
        if(index == -1):
            ans.append(m)
        else:
            index = index = index - key
            index = index % len(table)
            ans.append(table[index])
    return ans

def main():
    msg="I Love you!! zzz"
    key= 6

    msg_enc= my_enc(msg.encode(),key)
    print(msg_enc)
    msg_dec=my_dec(msg_enc,key)
    print(msg_dec)


main()