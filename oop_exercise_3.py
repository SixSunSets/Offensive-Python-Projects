class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True
    
    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f'\n[!] El vehículo con matrícula {self.matricula} no se puede alquilar')
    
    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f'\n[!] El vehículo con matrícula {self.matricula} no ha sido alquilado')

    def __str__(self):
        return f'Vehiculo(matricula={self.matricula}, modelo={self.modelo}, disponible={self.disponible})'

class Flota:

    def __init__(self):
        self.vehiculos = []

    def agregar_vechiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
    
    def alquilar_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()
    
    def devolver_vechiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()
    
    def __str__(self):
        return '\n'.join(str(vehiculo) for vehiculo in self.vehiculos)

if __name__ == '__main__':
    flota = Flota()

    flota.agregar_vechiculo(Vehiculo('BABDAS5','Toyota Corolla'))
    flota.agregar_vechiculo(Vehiculo('AFBASD2','Honda Civic'))

    print('\n[+] Flota inicial:\n')
    print(flota)

    flota.alquilar_vehiculo('BABDAS5')

    print(f'\n[+] Mostrando la flota después de haber alquilado el Toyota')
    print(flota)

    flota.devolver_vechiculo('BABDAS5')

    print(f'\n[+] Mostrando la flota después de devolver el Toyota')
    print(flota)

    flota.devolver_vechiculo('BABDAS5')