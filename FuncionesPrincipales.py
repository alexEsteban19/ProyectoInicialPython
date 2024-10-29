# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 16:55:34 2024

@author: DAM
"""
import funciones as fun
import funcionesAPI as api

contraseña = "a"
intentos = 3

# Inicialización de clientes y productos
clientes = [
    fun.Cliente("Alejandro", "52981068Q", 1500),
    fun.Cliente("Mario", "52951172C", 1600)
]

productos = [
    fun.Proteina(84993029, "Impact", "Isolate", 2, 90, "Brownie", 89.99),
    fun.Proteina(98765432, "MyProtein", "Whey", 2, 85, "Vainilla y canela", 41.90),
    fun.Creatina(34759832, "Bulk", "Monohidratada", 0.50, 95, "Fresa", 35.99, 3),
    fun.Proteina(56789078, "AreaProteica", "Isolate", 4, 85, "Chocolate y avellanas", 55.90),
    fun.Creatina(32342344, "Amix", "Clorhidratada", 5, 90, "Neutro", 26.99, 3)
]

miGym = fun.Gym("GYMRAT", 2006, clientes, productos)

def mostrar_menu_admin():
    return int(input("Bienvenido administrador, ¿qué desea gestionar?\n"
                     "CLIENTES\n1. Añadir clientes\n"
                     "2. Eliminar clientes\n"
                     "3. Modificar clientes\n"
                     "4. Mostrar Clientes Actuales\n"
                     "-----------------------------\n"
                     "PRODUCTOS\n5. Añadir producto\n"
                     "6. Borrar producto\n"
                     "7. Modificar productos\n"
                     "8. Mostrar productos actuales\n"
                     "-----------------------------\n"
                     "GIMNASIO\n9. Generar archivo del gimnasio\n"
                     "10. Salir del modo administrador\n"))

def gestionar_admin():
    global intentos
    while intentos > 0:
        intento_contra = input("Introduzca la contraseña:\n")
        if intento_contra == contraseña:
            while True:
                eleccion = mostrar_menu_admin()
                match eleccion:
                    case 1: miGym.añadirCliente(clientes)
                    case 2: miGym.borrarCliente(clientes)
                    case 3: miGym.modificarCliente(clientes)
                    case 4:
                        for cliente in clientes:
                            cliente.mostrarCliente()
                    case 5: miGym.añadirProducto(productos)
                    case 6: miGym.borrarProducto(productos)
                    case 7: miGym.modificarProducto(productos)
                    case 8:
                        for producto in productos:
                            producto.mostrarProducto()
                    case 9: miGym.guardarInfo()
                    case 10:
                        print("Saliendo del modo administrador...")
                        return
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")

    print("No hay más intentos. Saliendo...")

def mostrar_menu_usuario():
    return int(input("Bienvenido usuario, ¿qué desea gestionar?\n"
                     "CLIENTES\n1. Añadir clientes\n"
                     "2. Eliminar clientes\n"
                     "3. Modificar clientes\n"
                     "4. Mostrar Clientes Actuales\n"
                     "-----------------------------\n"
                     "PRODUCTOS\n5. Añadir producto\n"
                     "6. Borrar producto\n"
                     "7. Modificar productos\n"
                     "8. Mostrar productos actuales\n"
                     "-----------------------------\n"
                     "GIMNASIO\n9. Generar archivo del gimnasio\n"
                     "10. Salir\n"))

def gestionar_usuario():
    while True:
        eleccion = mostrar_menu_usuario()
        match eleccion:
            case 1: miGym.añadirCliente(clientes)
            case 2: miGym.borrarCliente(clientes)
            case 3: miGym.modificarCliente(clientes)
            case 4:
                for cliente in clientes:
                    cliente.mostrarCliente()
            case 5: miGym.añadirProducto(productos)
            case 6: miGym.borrarProducto(productos)
            case 7: miGym.modificarProducto(productos)
            case 8:
                for producto in productos:
                    producto.mostrarProducto()
            case 9: miGym.guardarInfo()
            case 10:
                print("Saliendo...")
                return