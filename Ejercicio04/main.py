from vocales import ContadorVocales

if __name__ == '__main__':
    archivo = "Ejercicio04/texto.txt"
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    for i in range(5):
        hilo = ContadorVocales(vocales[i], archivo)
        hilo.start()

    hilo.join()
    print("\n✅ Conteo de vocales finalizado.")