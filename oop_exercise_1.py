class Libro:
    def __init__(self,id_libro, autor, nombre_libro):
        self.id_libro = id_libro
        self.autor = autor
        self.nombre_libro = nombre_libro
        self.esta_prestado = False

    def __str__(self): # Método especial
        return f"Libro({self.id_libro}, {self.autor}, {self.nombre_libro})"
    
    def __repr__(self):
        return self.__str__()

class Biblioteca:
    def __init__(self):
        self.libros = {} # {1: Libro(1, Marcelo, Titulo del libro1), 2: Libro(...)}

    def agregar_libro(self, libro):
        if libro.id_libro not in self.libros: # Si el libro no existe en el diccionario, lo agrega
            self.libros[libro.id_libro] = libro
        else:
            print(f"\n[!] No es posible agregar el libro con ID {libro.id_libro}")

    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n[!] No es posible prestar el libro con ID {id_libro}")
    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]

    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if libro.esta_prestado]

class BibliotecaInfantil(Biblioteca):
    def __init__(self):
        super().__init__() # Crea el diccionario self.libros y cualquier otro atributo de la superclase
        self.libros_para_ninos = {} # {1: False, 2: True}
    
    def agregar_libro(self, libro, es_para_ninos):
        super().agregar_libro(libro) # La operatoria la hará la misma función de la superclase
        self.libros_para_ninos[libro.id_libro] = es_para_ninos

    def prestar_libro(self, id_libro, es_nino):
        if id_libro in self.libros and self.libros_para_ninos[id_libro] == es_nino and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n[!] No es posible prestar el libro con ID {id_libro}")

    @property
    def mostrar_estado_libros_para_ninos(self):
        return self.libros_para_ninos
    
if __name__ == '__main__':

    biblioteca = BibliotecaInfantil()
    
    libro1 = Libro(1, "Marcelo", "Titulo del libro1")
    libro2 = Libro(2, "Javier", "Titulo del libro2")

    biblioteca.agregar_libro(libro1, es_para_ninos=False)
    biblioteca.agregar_libro(libro2, es_para_ninos=True)
    
    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    biblioteca.prestar_libro(1, es_nino=False)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
    print(f"\n[+] Libros :prestados {biblioteca.mostrar_libros_prestados}")
    print(f"\n[+] Libros para niños: {biblioteca.mostrar_estado_libros_para_ninos}")


