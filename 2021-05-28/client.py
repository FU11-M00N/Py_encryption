import mynetlib

def do_work_client(client):
    print('클라이언트의 일 입니당근당근')
    cmd = '하위염소'
    mynetlib.my_send(cmd, client)
    
    cmd_r = mynetlib.my_recv(1024, client)
    print('서버가 말하는디여? : ',cmd_r)
    
mynetlib.run_client('localhost',2025,do_work_client)