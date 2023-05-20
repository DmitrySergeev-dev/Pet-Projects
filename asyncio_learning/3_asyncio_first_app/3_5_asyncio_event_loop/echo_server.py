"""
 Имеется одна сопрограмма, listen_for_connection, прослушивающая порт. Как только
клиент подключился, она запускает задачу echo для этого клиента, которая ожидает поступления данных и отправляет их обратно клиенту.

Это приложение позволяет конкурентно прослушивать нескольких
клиентов и отправлять им данные. Под капотом используются все те
же селекторы, которые мы видели раньше, так что потребление про-
цессора остается низким.
Мы написали полнофункциональный эхо-сервер, пользуясь только
asyncio! Но нет ли в нашей реализации дефектов? Есть – мы не обрабатываем ошибки в задаче echo.
"""

import asyncio
from asyncio import AbstractEventLoop
import socket


async def listen_for_connections(
        server_socket: socket, loop: AbstractEventLoop
):
    while True:
        connection, address = await loop.sock_accept(server_socket)
        connection.setblocking(False)
        print(f'Получен запрос на подключение от "{address}"')
        asyncio.create_task(echo(connection, loop))


async def echo(
        connection: socket, loop: AbstractEventLoop
):
    while data := await loop.sock_recv(connection, 1024):
        await loop.sock_sendall(connection, data)


async def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = ('127.0.0.1', 8000)
    server_socket.setblocking(False)
    server_socket.bind(server_address)
    server_socket.listen()

    await listen_for_connections(server_socket, asyncio.get_event_loop())

asyncio.run(main())


