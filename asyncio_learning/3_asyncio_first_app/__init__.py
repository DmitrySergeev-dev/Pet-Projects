"""
Краткое содержание главы

Применение сокетов для передачи данных по сети.

Применение telnet для взаимодействия с приложением на
основе сокетов.

Использование селекторов для построения простого цикла
событий для неблокирующих сокетов.

Создание неблокирующего эхо-сервера, допускающего
несколько подключений.

Обработка исключений в задачах.

Включение специальной логики остановки в приложение
asyncio.


В главах 1 и 2 мы познакомились с сопрограммами, задачами и цик-
лом событий, а также узнали, как выполнять длительные операции
конкурентно, и изучили некоторые API asyncio, предназначенные для
этой цели. Но до сих пор мы лишь эмулировали длительные операции
с по мощью функции sleep.

Не желая ограничиваться одними демонстрационными приложе-
ниями, воспользуемся некоторыми реальными блокирующими опе-
рациями, чтобы показать, как можно создать сервер, способный об-
рабатывать несколько пользователей одновременно.
Мы сделаем это, используя только один поток, в результате чего приложение окажется проще и менее требовательным к ресурсам, чем альтернативные
решения с несколькими потоками и процессами.
Мы применим все, что узнали о сопрограммах, задачах и API asyncio, для написания командного эхо-сервера, в котором будут использоваться сокеты. К концу главы вы сможете сами создавать сетевые приложения на основе asyncio, умеющие одновременно обслуживать несколько пользователей в одном потоке.
Сначала рассмотрим, как отправлять и принимать данные с помощью блокирующих сокетов.
Мы попробуем с их помощью построить эхо-сервер, обслуживающий несколько клиентов.
И убедимся, что хорошо сделать это в одном потоке невозможно.
Затем поговорим о том, как разрешить возникшие проблемы, сделав сокеты неблокирующими и воспользовавшись системой уведомлений, входящей в состав операционной системы.
Это поможет понять, как работает механизм, лежащий в основе цикла событий. После этого мы применим сопрограммы с неблокирующими сокетами asyncio, чтобы правильно реализовать обслуживание нескольких пользователей, которые одновременно отправляют и принимают сообщения.
Наконец, мы добавим специальную логику остановки, оставляющую некоторое
время для завершения уже начатой работы.
"""