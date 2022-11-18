from datetime import datetime
import json
import os
import socket 
import subprocess
import time
from typing import List
import base64

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("0.0.0.0", 5000))
print("Success connect")

def _send(socket :socket.socket, data :str):
    socket.send(json.dumps(data).encode())

def _recv(socket :socket.socket, n_byte :int = 4096):
    
    b_data = b''
    
    while True:
        try:
            b_data += socket.recv(n_byte)
            return json.loads(b_data)
        except ValueError:
            continue
    
while True:
    data = input(">> ")
    _send(client_socket,data)
    data = _recv(client_socket)
    print(data)
    
    