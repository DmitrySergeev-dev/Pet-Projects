"""
В главе 1 мы познакомились с сокетами. Напомним, что сокет – это
способ читать и записывать данные по сети. Можно считать, что со-
кет – своего рода почтовый ящик: мы кладем в него письмо, а оно за-
тем доставляется по адресу получателя. Получатель сможет прочесть
сообщение и, возможно, отправит ответ.
Прежде всего создадим главный сокет, называемый серверным.
Он будет принимать сообщения от клиентов, желающих установить
с нами соединение. После того как серверный сокет подтвердит за-
прос на подключение, мы создаем сокет, предназначенный для взаи-
модействия с клиентом. Таким образом, сервер становится похож на
почтовое отделение не с одним, а с несколькими почтовыми ящика-
ми. Что касается клиента, можно по-прежнему считать, что он владе-
ет только одним почтовым ящиком, поскольку открывает для взаи-
модействия с нами один сокет. Когда клиент подключается к серверу,
мы предоставляем ему почтовый ящик, а затем используем его для
получения и отправки сообщений (рис. 3.1).
Такой сервер можно создать с помощью встроенного в Python мо-
дуля socket, предоставляющего средства для чтения, записи и управ-
ления сокетом. Для начала напишем простой сервер, который прослу-
шивает порт, куда поступают запросы на подключение от клиентов,
и печатает сообщения об успешном подключении. С этим сокетом бу-
дут ассоциированы имя хоста и порт, он станет главным «серверным
сокетом», с которым могут взаимодействовать клиенты.
"""