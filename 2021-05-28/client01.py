# -*- coding: utf-8 -*-
"""
Created on Fri May 28 10:57:30 2021

@author: user
"""

import mynetlib

def do_work_client(client):
    print('클라이언트의 일 입니당근당근')
    
mynetlib.run_client('localhost',2026,do_work_client)