import my



def main():
    
    hv1= my.get_hash('test1.py')
    hv2= my.get_hash('test1.py.txt')


    if (hv1 == hv2):
        print("동일한 내용의 파일")
    else:
        print("다른 내용의 파일")
    pass
    hv1_txt = base64.b64encode(hv1)
    hv2_txt = base64.b64decode(hv2)


main()