# Serializacion - deserializacion
# Convertir un objeto a una secuencia de bytes para el almacenado en disco, transmisión a través de red
# Objeto: Lista, diccionarios, tuplas, cadenas
# pickle
# Os
# os.name = {'nt': 'windows', 'posix': 'linux'}
# Pickle
# with open("notas.pkl", "rb") as f:
#   mis_notas = pickle.load(f)

import os
from gestor_notas import GestorNotas

def main():
    gestor = GestorNotas()

    while True:
        print('\n==========\nMENU\n==========')
        print('1. Agregar una nota')
        print('2. Leer todas las notas')
        print('3. Buscar por una nota')
        print('4. Eliminar una nota')
        print('5. Salir')

        opcion = input("\n[+] Elige una opción: ")

        if opcion == '1':
            contenido = input('\n[+] Contenido de la nota: ')
            gestor.agregar_nota(contenido)

        elif opcion == '2':
            notas = gestor.leer_notas()
            print('[+] Mostrando todas las notas almacenadas:\n')
            for i,nota in enumerate(notas):
                print(f'{i}: {nota}')
        
        elif opcion == '3':
            texto_busqueda = input('\n[+] Ingresa el texto a buscar como criterio en las notas: ')
            notas = gestor.buscar_nota(texto_busqueda)
            print('\nMostrando las notas que coinciden con el criterio de busqueda:\n')

            for i, nota in enumerate(notas):
                print(f'{i}: {nota}')

        elif opcion == '4':
            indice = int(input('\n[+] Indique el índice de la nota a eliminar: '))
            gestor.eliminar_nota(indice)

        elif opcion == '5':
            break
        else:
            print('\n[!] La opción indicada es incorrecta\n')
        
        input('\n[+] Presiona <Enter> para continuar...')

        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()