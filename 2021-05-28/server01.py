# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:51:04 2021

@author: user
"""

import mynetlib

def do_work_server(client,addr):
    print('서버의 일이다!')
    
mynetlib.run_server(2025, do_work_server,1)