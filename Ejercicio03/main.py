from adivinar import Adivinador, Comprobador
import random

if __name__ == '__main__':
    nombres = ['Amaro', 'Auri', 'Jenri', 'Messi', 'Ronaldo', 'Fekir', 'Isco', 'Sabaly', 'Lo Celso', 'Antony']
    comprobador = Comprobador()
    for i in range(10):
        hilo = Adivinador(nombres[i], comprobador)
        hilo.start()