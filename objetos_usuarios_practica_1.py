class usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    
    def hacerCompra(self, monto):
        self.saldo_pagar += monto

    def pagar_tarjeta(self, monto):
        self.saldo_pagar -= monto

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a pagar: {self.saldo_pagar}")

    def transferir_deuda(self, otro_usuario, monto):
        if monto <= self.saldo_pagar:
            self.saldo_pagar -= monto
            otro_usuario.saldo_pagar += monto
        else:
            print(f"No puede transferir mas deuda de la que tiene. Deuda de {self.nombre} {self.apellido} es {self.saldo_pagar}")
    
    def pagar_total(self):
        print(f"Pagando totalidad de deuda de {self.saldo_pagar} de {self.nombre} {self.apellido}...")
        self.saldo_pagar -= self.saldo_pagar
        print(f"Deuda pagada. Saldo de {self.nombre} {self.apellido} es: {self.saldo_pagar}")


jon = usuario("Jon", "Snow", "jon@gmail.com")
khalesi = usuario("Daenerys", "Targaryen", "reina@gmail.com")
arya = usuario("Arya", "Stark", "ary@gmail.com")

# jon.hacerCompra(5000)
# jon.hacerCompra(7000)
# jon.pagar_tarjeta(8500)
# jon.mostrar_saldo_usuario()

# arya.hacerCompra(300)
# arya.pagar_tarjeta(300)
# arya.mostrar_saldo_usuario()

# khalesi.hacerCompra(50000)
# khalesi.hacerCompra(10000)
# khalesi.hacerCompra(20000)
# khalesi.pagar_tarjeta(25000)
# khalesi.pagar_tarjeta(25000)
# khalesi.pagar_tarjeta(10000)
# khalesi.pagar_tarjeta(20000)
# khalesi.mostrar_saldo_usuario()

# jon.transferir_deuda(arya, 500)
# jon.mostrar_saldo_usuario()
# arya.mostrar_saldo_usuario()

# jon.pagar_total()
# arya.pagar_total()

