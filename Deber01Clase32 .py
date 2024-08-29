# Definir listas para almacenar los nombres de los usuarios y sus saldos.
usuarios = []
saldos = []

def registrar_usuario():
    nombre = input("Ingrese su nombre para registrar: ").strip()
    if nombre in usuarios:
        print("El usuario ya esta registrado.")
    else:    
        usuarios.append(nombre) 
        saldos.append(0.00)
        print(f"usuario {nombre} agregado correctamente")

def depositar():
    nombre = input("Introduce el nombre del usuario: ").strip()
    if nombre in usuarios:
        index = usuarios.index(nombre)
        monto = float(input("Introduce el monto a depositar: "))
        saldos[index] += monto
        print(f"Depósito de {monto} realizado con éxito.")
    else:
        print(f"Usuario {nombre} no existe.")

def retirar():
    nombre = input("Ingrese el nombre del usuario: ").strip()
    if nombre in usuarios:
        index = usuarios.index(nombre)
        retiro = float(input("Ingrese el monto de retiro: "))
        if retiro > saldos[index]:
            print("Saldo insuficiente para retirar.")
        else:
            saldos[index] -= retiro
            print(f"Retiro de {retiro} realizado con éxito.")
    else:
        print("Usuario no existe en el sistema.")
    
def consultar_saldo():
    nombre = input("Ingrese su nombre para consultar el saldo: ").strip()
    if nombre in usuarios:
        index = usuarios.index(nombre)
        print(f"El saldo de {nombre} es {saldos[index]}.")
    else:
        print("Usuario no existe en el sistema.")

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar Usuario")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Consultar Saldo")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            depositar()
        elif opcion == '3':
            retirar()
        elif opcion == '4':
            consultar_saldo()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

menu()