def test1():
    fh = open('test2.py','rb')

    data = fh.read(100)

    while data:
        print(len(data))

        data =fh.read(100)

#test1()


def test2():
    fh1= open('test1.py','rb')

    fh2= open('test1.py.txt','wb')    
        
    data = fh1.read(100)

    while data:
        fh2.write(data)
        data = fh1.read(100)
    pass

test2()