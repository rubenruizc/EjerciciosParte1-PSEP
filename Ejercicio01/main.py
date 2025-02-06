from trabajadores import Trabajadores

from threading import Thread

trabajadores = ["Rubén","Ruiz","Castaño","Suárez","Calle"]

if __name__ == "__main__":
   for i in range (0,5):
      t = Trabajadores(trabajadores[i])
      t.start()
