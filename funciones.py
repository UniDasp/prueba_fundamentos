import os
import time
import random

def clear():
    return os.system("cls")

def wait(s):
    return time.sleep(s)

def menu():
    while True:
        print("1.- Registrar cliente")
        print("2.- Listar clientes registrados")
        print("3.- Registrar compra")
        print("4.- Enviar información de puntos acumulados a un cliente")
        print("5.- Salir")

        interaction = input("Ingresa tu opción: ")

        if interaction == "1":
            registrar()
        elif interaction == "2":
            listar_clientes()
        elif interaction == "3":
            registrar_compra()
        elif interaction == "4":
            resumen_cliente()
        elif interaction == "5":
            break
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 5.")

def registrar():
    with open('datos.txt', 'a', encoding='utf-8') as archivo:
        nombre = input("Ingresa el nombre del cliente: ")
        apellidos = input("Ingresa el apellido del cliente: ")
        correo = input("Ingresa el correo electrónico del cliente: ")
        id_cliente = random.randint(1, 1000) # Un numero del 1 al 1000 que va a funcinar como id XD

        datos = f'{{"id": {id_cliente}, "nombre": "{nombre} {apellidos}", "correo": "{correo}"}}\n'
        archivo.write(datos)
        print(f"Cliente registrado con ID: {id_cliente}")

def listar_clientes():
    try:
        with open('datos.txt', 'r', encoding="utf-8") as archivo:
            print("ID \t Nombre \t Correo")
            for linea in archivo:
                cliente = eval(linea)
                print(f"{cliente['id']} \t {cliente['nombre']} \t {cliente['correo']}")
    except FileNotFoundError:
        print("No se encontró el archivo de datos.")

def registrar_compra():
    try:
        with open('datos.txt', 'r', encoding='utf-8') as archivo:
            contenido = archivo.readlines()

        id_cliente = input("Ingrese el ID del cliente que realizó la compra: ")
        fecha = input("Ingrese la fecha de la compra (YYYY-MM-DD): ")
        monto = float(input("Ingrese el monto total de la compra: "))

        puntos_acumulados = int(monto * 0.01)

        with open('compras.txt', 'a', encoding='utf-8') as archivo_compras:
            compra = f'{{"id_cliente": {id_cliente}, "fecha": "{fecha}", "monto": {monto}, "puntos_acumulados": {puntos_acumulados}}}\n'
            archivo_compras.write(compra)

        print(f"Compra registrada correctamente. Puntos acumulados: {puntos_acumulados}")
    
    except FileNotFoundError:
        print("No se encontró el archivo de datos.")

def resumen_cliente():
    id_cliente = input("Ingrese el ID del cliente para enviar la información de puntos acumulados: ")

    try:
        with open('compras.txt', 'r', encoding='utf-8') as archivo_compras:
            lineas = archivo_compras.readlines()

        with open(f'RESUMEN_CLIENTE_ID_{id_cliente}.txt', 'w', encoding='utf-8') as archivo_resumen:
            archivo_resumen.write(f"ID CLIENTE: {id_cliente}\n")

            total_puntos = 0
            for linea in lineas:
                compra = eval(linea)
                if compra['id_cliente'] == int(id_cliente):
                    archivo_resumen.write(f"Fecha de Compra: {compra['fecha']} \t Monto Total: ${compra['monto']} \t Puntos: {compra['puntos_acumulados']}\n")
                    total_puntos += compra['puntos_acumulados']
            
            archivo_resumen.write(f"\nPUNTOS TOTALES A CANJEAR: {total_puntos} pesos\n")

        print(f"Archivo de resumen creado: RESUMEN_CLIENTE_ID_{id_cliente}.txt")

    except FileNotFoundError:
        print("No se encontró el archivo de compras.")

menu()
