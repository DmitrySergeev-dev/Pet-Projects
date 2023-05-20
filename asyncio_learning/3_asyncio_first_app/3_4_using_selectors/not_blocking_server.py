"""
Эта программа печатает сообщение «Событий нет, подожду еще!»
примерно каждую секунду, пока не будет получено событие подклю-
чения. После этого мы регистрируем сокет для прослушивания собы-
тий чтения. Теперь, как только клиент отправит нам данные, селектор
вернет событие готовности данных и мы сможем прочитать их с по-
мощью функции socket.recv. Мы написали полнофункциональный
эхо-сервер, поддерживающий нескольких клиентов. У него нет про-
блем с блокированием, поскольку чтение или запись производятся
только тогда, когда имеются данные. Он почти не потребляет про-
цессорного времени, так как мы пользуемся эффективной системой
уведомления о событиях, которая реализована внутри операционной
системы.

То, что мы сделали, во многом напоминает действия, выполняемые
циклом событий под капотом. В данном случае события – получение
данных через сокет. Каждая итерация нашего цикла событий и цик-
ла событий asyncio запускается либо событием сокета, либо срабаты-
ванием таймера. В цикле событий asyncio в любом из этих случаев
активируется ожидающая сопрограмма и выполняется до конца или
до следующего предложения await. Если await встречается в сопро-
грамме, где используется неблокирующий сокет, то она регистрирует
этот сокет в системном селекторе и запоминает, что эта сопрограмма
приостановлена в ожидании результата.
"""

import selectors
import socket

selector = selectors.DefaultSelector()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 8000)
server_socket.setblocking(False)
server_socket.bind(server_address)
server_socket.listen()

selector.register(server_socket, selectors.EVENT_READ)
while True:
    events: list[tuple[selectors.SelectorKey, int]] = selector.select(timeout=1)
    if len(events) == 0:
        print("Событий нет, подожду еще!")
    for event, _ in events:
        event_socket = event.fileobj
        if event_socket == server_socket:
            connection, address = server_socket.accept()
            connection.setblocking(False)
            print(f'Получен запрос на подключение от "{address}"')
            selector.register(connection, selectors.EVENT_READ)
        else:
            data = event_socket.recv(1024)
            print(f'Получены данные от {connection}: {data}')
            event_socket.send(data)

