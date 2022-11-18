import socket, json
# domain:5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()

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

try :
    while True:
        client_socket, addr = server_socket.accept()
        print('Connection from', addr)
        while True:
            request = _recv(client_socket)

            if not request:
                break
            else:
                print(request)
                response = request
                _send(client_socket, response)
        print('Outside inner while loop')
except KeyboardInterrupt as e:
    server_socket.shutdown(socket.SHUT_RDWR)
    server_socket.close()
    