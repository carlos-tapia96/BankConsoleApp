class Persona():
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido



##  CLASE CLIENTE   ##
class Cliente(Persona):
    def __init__(self,nombre,apellido,numero_cuenta,balance=0):
        super().__init__(nombre,apellido)
        self.numero_cuenta=numero_cuenta
        self.balance=balance

    def __str__(self):
        return f'Tu nombre es: {self.nombre} {self.apellido} \nBalance de cuenta {self.numero_cuenta} : ${self.balance}'



    def imprimir_datos(self):
        nombre=self.nombre
        apellido=self.apellido

    def depositar(self,monto_depositar):
        self.balance+=monto_depositar
        print("DEPOSITO ACEPTADO")


    def retirar(self,monto_retirar):
        if self.balance>=monto_retirar:
            self.balance-=monto_retirar
            print("RETIRO REALIZADO")
        else:
            print("FONDOS INSUFICIENTES")

##  OPCION PARA DEPOSITAR, RETIRAR O SALIR
def crear_cliente():
    nombre_cl=input("Ingrese su nombre: ")
    apellido_cl=input("Ingrese su apellido: ")
    numero_cuenta=input("Ingrese su numero de cuenta: ")
    cliente = Cliente(nombre_cl,apellido_cl,numero_cuenta)
    return cliente

def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    opcion = 0
    while opcion != 'S':
        print("Elije: Depositar (D),Retirar (R), o Salir (S)")
        opcion=input()
        if opcion == 'D':
            monto_dep=int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_dep)
        elif opcion =='R':
            monto_Ret=int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_Ret)
        print(mi_cliente)
    print("Gracias por operar en el banco Py")

inicio()