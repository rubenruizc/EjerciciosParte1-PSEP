from threading import Thread,Barrier
import time
import random



class Trabajadores(Thread):
    def __init__(self,nombre):
        Thread.__init__(self)
        self.nombre = nombre
        

    def run(self):
        while True:
            print("Soy", self.nombre, "y estoy trabajando")
            time.sleep(random.random())
            print("Soy", self.nombre, "y estoy descansando")
        

        
        