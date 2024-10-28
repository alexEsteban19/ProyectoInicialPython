# -*- coding: utf-8 -*-

import funciones as fun

contraseña = "a"

cliente1 = fun.Cliente("Alejandro", "52981068Q", 1500)
cliente2 = fun.Cliente("Mario", "52951172C", 1600)

producto1 = fun.Proteina(84993029, "Impact", "Isolate",
                         2, 90, "Brownie", 89.99)
producto2 = fun.Proteina(98765432, "MyProtein", "Whey", 2,
                         85, "Vainilla y canela", 41.90)
producto3 = fun.Creatina(34759832, "Bulk", "Monohidratada",
                         0.50, 95, "Fresa", 35.99, 3)
producto4 = fun.Proteina(56789078, "AreaProteica", "Isolate",
                         4, 85, "Chocolate y avellanas", 55.90)
producto5 = fun.Creatina(32342344, "Amix", "Clorhidratada",
                         5, 90, "Neutro", 26.99, 3)


clientes = []
clientes.append(cliente1)
clientes.append(cliente2)

productos = []
productos.append(producto1)
productos.append(producto2)
productos.append(producto3)
productos.append(producto4)
productos.append(producto5)

miGym = fun.Gym("GYMRAT", 2006, clientes, productos)
while True:
    opcion = int(input(f"Bienvenido a {miGym.nombre}, ¿es usted administrador(1) o usuario(2)?\n"))
    
    if opcion == 1:
        intentoContra = input("Ha elegido la opción de ser administrador.\nPor favor, introduzca la contraseña para acceder a la gestión del gimnasio.\n")
        while True:
             if intentoContra == contraseña:
    
                  eleccion = int(input("Bienvenido administrador, ¿qué desea gestionar?\nCLIENTES\n1. Añadir clientes \n2. Eliminar clientes\n3. Modificar clientes\n4. Mostrar Clientes Actuales\n-----------------------------\nPRODUCTOS\n5. Añadir producto\n6. Borrar producto\n7. Modificar productos\n8. Mostrar productos actuales\n-----------------------------\nGIMNASIO\n9. Generar archivo del gimnasio\n10. Salir\n"))
    
                  match eleccion:
                      case 1:
                          print()
                          miGym.añadirCliente(clientes)
    
                      case 2:
                          print()
                          miGym.borrarCliente(clientes)
    
                      case 3:
                          print()
                          miGym.modificarCliente(clientes)
    
                      case 4:
                          print()
                          for cliente in clientes:
                              cliente.mostrarCliente()
                              print("\n\n\n")    
    
                      case 5:
                          print()
                          miGym.añadirProducto(productos)
    
                      case 6:
                          print()
                          miGym.borrarProducto(productos)
    
                      case 7:
                          print()
                          miGym.modificarProducto(productos)
    
                      case 8:
                          print()
                          for producto in productos:
                              producto.mostrarProducto()
                          print("\n\n\n")    
    
                      case 9:
                           miGym.guardarInfo()
    
                      case 10:
                          print("a")
                          break
    
             elif intentoContra != contraseña:
                 print("Contraseña incorrecta\n")
                 break
    if opcion == 2:
        while True:    
                  eleccion = int(input("Bienvenido usuario, ¿qué desea gestionar?\nCLIENTES\n1. Añadir clientes \n2. Eliminar clientes\n3. Modificar clientes\n4. Mostrar Clientes Actuales\n-----------------------------\nPRODUCTOS\n5. Añadir producto\n6. Borrar producto\n7. Modificar productos\n8. Mostrar productos actuales\n-----------------------------\nGIMNASIO\n9. Generar archivo del gimnasio\n10. Salir\n"))
    
                  match eleccion:
                      case 1:
                          print()
                          miGym.añadirCliente(clientes)
    
                      case 2:
                          print()
                          miGym.borrarCliente(clientes)
    
                      case 3:
                          print()
                          miGym.modificarCliente(clientes)
    
                      case 4:
                          print()
                          for cliente in clientes:
                              cliente.mostrarCliente()
                              print("\n\n\n")    
    
                      case 5:
                          print()
                          miGym.añadirProducto(productos)
    
                      case 6:
                          print()
                          miGym.borrarProducto(productos)
    
                      case 7:
                          print()
                          miGym.modificarProducto(productos)
    
                      case 8:
                          print()
                          for producto in productos:
                              producto.mostrarProducto()
                          print("\n\n\n")    
    
                      case 9:
                           miGym.guardarInfo()
    
                      case 10:
                          print("a")
                          break

    break

     
