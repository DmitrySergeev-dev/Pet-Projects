import socket

server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# Функция socket принимает два параметра. Первый, socket.AF_INET, – тип адреса, в данном случае адрес будет содержать имя хоста и номер порта. Второй socket.SOCK_STREAM, означает, что для взаимо-
# действия будет использоваться протокол TCP.
server_socket.setsockopt(socket.SOL_SOCKET,
                         socket.SO_REUSEADDR, 1) # чтобы установить флаг
# SO_REUSEADDR в 1. Это позволит повторно использовать номер порта,
# после того как мы остановим и заново запустим приложение, из-
# бегнув тем самым ошибки «Адрес уже используется». Если этого не
# сделать, то операционной системе потребуется некоторое время, что-
# бы освободить порт, после чего приложение сможет запуститься без
# ошибок

# Функция socket.socket создает сокет, но начать взаимодействие по
# нему мы еще не можем, потому что сокет не привязан к адресу, по
# которому могут обращаться клиенты (у почтового отделения должен
# быть адрес!). В данном случае мы привяжем сокет к адресу своего соб-
# ственного компьютера 127.0.0.1 и выберем произвольный порт 8000:
server_address = ('127.0.0.1', 8000)
server_socket.bind(server_address)

# Теперь у сокета есть адрес – 127.0.0.1:8000. Клиенты смогут исполь-
# зовать этот адрес для отправки данных нашему серверу, а если мы
# отправим данные клиенту, то клиент увидит адрес, с которого они
# пришли.
# Далее мы должны активно прослушивать запросы от клиентов, желающих подключиться к нашему серверу. Для этого вызывается
# метод сокета listen. Затем мы ждем запроса на подключение с помощью метода accept. Этот метод блокирует программу до получения запроса, после чего возвращает объект подключения и адрес подключившегося клиента.
# Объект подключения – это еще один сокет, который можно использовать для чтения данных от клиента и записи адресованных ему данных.

server_socket.listen()
client_socket, client_address = server_socket.accept()
# Теперь у нас есть все необходимое для создания серверного приложения на основе сокетов, которое будет ждать запросов на подключение и печатать сообщение, когда запрос придет.
print(f'Получен запрос на подключение от {client_address}!')



