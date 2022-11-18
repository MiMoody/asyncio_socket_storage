import asyncio, socket
import json
from socket import AddressFamily
from business_logic.command import * 
from business_logic.exceptions import *


class SocketServer:
    
    def __init__(self, 
                 host :str, 
                 port :int,
                 family :AddressFamily = socket.AF_INET,
                 type  = socket.SOCK_STREAM):
        """ Инициалиазация объекта сервера """
        
        print("Инициалиазация объекта сервера")
        self._host = host
        self._port = port
        self._server = socket.socket(family, type)
        self._server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    async def _client_process(self, client_socket :socket.socket):
        """ Асинхронное взаимодействие с клиентом """
        
        while True:
            command :str = await self._recv(client_socket)
            try:
                command_split = validate_command(command)
                result = await self._loop.run_in_executor(None, execute_command, command_split)
                await self._send(client_socket, result)
            except Exception as e:
                await self._send(client_socket, e.value)
    
    async def _server_process(self,):
        """ Асинхронное ожидание подключений к серверу """
        
        self._loop = asyncio.get_event_loop()
        while True:
            client_socket, remote_addr = await self._loop.sock_accept(self._server)
            print("Подключение клиента --> ", remote_addr)
            self._loop.create_task(self._client_process(client_socket))
    
    async def _send(self, socket :socket.socket, data :str):
        """ Асинхронная отправка данных через сокет"""
        
        await self._loop.sock_sendall(socket, json.dumps(data).encode())

    async def _recv(self, socket :socket.socket, n_byte :int = 4096):
        """ Асинхронное получение данных через сокет"""
        
        b_data = b''
        while True:
            try:
                b_data += await self._loop.sock_recv(socket, n_byte)
                return json.loads(b_data)
            except ValueError:
                continue
            
    def run(self):
        """ Блокирующий запуск сервера """
        
        self._server.bind((self._host, self._port))
        self._server.listen()
        self._server.setblocking(False)
        asyncio.run(self._server_process())
        

if __name__ == "__main__":
    
    try:
        server = SocketServer("0.0.0.0", 5000)
        server.run()
    except:
        print("Завершение ...")
        exit()