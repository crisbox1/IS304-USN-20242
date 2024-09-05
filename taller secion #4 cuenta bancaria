class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se depositaron {cantidad} unidades. Nuevo saldo: {self.saldo}.")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Se retiraron {cantidad} unidades. Nuevo saldo: {self.saldo}.")
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser positiva.")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.titular}: {self.saldo}")

class CuentaCorriente(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, descubierto_permitido=0):
        super().__init__(titular, saldo_inicial)
        self.descubierto_permitido = descubierto_permitido

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo + self.descubierto_permitido:
                self.saldo -= cantidad
                print(f"Se retiraron {cantidad} unidades. Nuevo saldo: {self.saldo}.")
            else:
                print("Fondos insuficientes y descubierto excedido.")
        else:
            print("La cantidad a retirar debe ser positiva.")
