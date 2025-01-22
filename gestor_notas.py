import pickle
from notas import Nota

class GestorNotas:
    def __init__(self, archivo_notas = 'notas.pkl'):
        self.archivo_notas = archivo_notas

        try:
            with open(self.archivo_notas, 'rb') as f:
                self.notas = pickle.load(f)
        except FileNotFoundError:
            self.notas = []
    def guardar_notas(self):
        with open(self.archivo_notas, 'wb') as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.guardar_notas()

    def leer_notas(self):
        return self.notas

    def eliminar_nota(self, indice):
        if indice < len(self.notas):
            del self.notas[indice]
            self.guardar_notas()
            print(f'\n[+] La nota {indice} ha sido eliminada')
        else:
            print(f'\n[!] No existe la nota con indice {indice}')

    def buscar_nota(self, texto_busqueda):
        return [nota for nota in self.notas if nota.coincide(texto_busqueda)]
       