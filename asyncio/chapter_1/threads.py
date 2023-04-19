import threading
from threading import Thread


def hello_from_thread():
    print(f'Привет от потока {threading.current_thread()}!\n')


hello_thread = Thread(target=hello_from_thread)
hello_thread.start()

total_threads = threading.active_count()
thread_name = threading.current_thread().name

print(f'В данный момент Python выполняет {total_threads} '
      f'поток(ов) \n')
print(f'Имя текущего потока {thread_name}\n')
hello_thread.join()