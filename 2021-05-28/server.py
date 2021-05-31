import mynetlib

def do_work_server(client,addr):
    print('서버의 일이다!')
    cmd_r = mynetlib.my_recv(1024, client)
    print('클라이언트가 말하는디? : ', cmd_r)
    cmd_s = cmd_r + 'serverrrrrrrrrr'
    mynetlib.my_send(cmd_s,client)
    
mynetlib.run_server(2030, do_work_server,1)