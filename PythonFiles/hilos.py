import threading
import random
import time

def aleatorio():
    sec = 2+(random.random()*3)
    time.sleep(sec)
    print(f'{threading.current_thread().name} {threading.get_native_id()} Tiempo : {sec} segundos')

for _ in range(5):
    hilo = threading.Thread(target=aleatorio)
    hilo.start()

print(f'{threading.current_thread().name} {threading.get_native_id()}')
