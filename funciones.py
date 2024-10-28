# -*- coding: utf-8 -*-
import json

class Cliente:
    
    def __init__(self, nombre, dni, saldoCuenta):
        self.nombre = nombre
        self.dni = dni
        self.saldoCuenta = saldoCuenta
    
    def mostrarCliente(self):
        return f"Nombre del cliente: {self.nombre}\nDNI del cliente: {self.dni}\nSaldo del cliente: {self.saldoCuenta}€\n----------------------------"
        
        
    def restarSaldo(self, saldo):
        if saldo < self.saldoCuenta:
            self.saldoCuenta -= saldo
            print("Saldo retirado con éxito")
        else:
            print("No tiene suficiente saldo")
    
    def to_dict(self):
        return {"Nombre": self.nombre,
                "DNI": self.dni,
                "Saldo del cliente": self.saldoCuenta
                }

class Producto:
    
    def __init__(self, idprod, marca, tipo, peso, pureza, sabor, precio):
        self.idprod = idprod
        self.marca = marca
        self.tipo = tipo
        self.peso = peso
        self.pureza = pureza
        self.sabor = sabor
        self.precio = precio
        
    def mostrarProducto(self):
        return f"ID del producto: {self.idprod}\nMarca del producto: {self.marca}\nTipo de producto: {self.tipo}\nPeso del producto en KG: {self.peso} KG\nPorcentaje de pureza del producto: {self.pureza}%\nSabor: {self.sabor}\nPrecio: {self.precio}€"
    
    def to_dict(self):
        return {"ID_Producto": self.idprod,
                "Marca": self.marca,
                "Tipo": self.tipo,
                "Peso": self.peso,
                "Pureza": self.pureza,
                "Sabor": self.sabor,
                "Precio": self.precio
                }
    
class Proteina(Producto):
    
    def __init__(self, idprod, marca, tipo, peso, pureza, sabor, precio):
        super().__init__(idprod, marca, tipo, peso, pureza, sabor, precio)
        
    def mostrarProducto(self):
        print("PROTEINA\n")
        return super().mostrarProducto() + "\n----------------------------"

    def to_dict(self):
        return super().to_dict()
    
class Creatina(Producto):
    
    def __init__(self, idprod, marca, tipo, peso, pureza, sabor, precio, dosisMax):
        super().__init__(idprod, marca, tipo, peso, pureza, sabor, precio)
        self.dosisMax = dosisMax
            
    def mostrarProducto(self):
        print("CREATINA\n")
        return f"{super().mostrarProducto()}\nDosis diaria máxima: {self.dosisMax}g\n----------------------------"
    
    def to_dict(self):
        return super().to_dict(), {"DosisMax": self.dosisMax}
        
class Gym: 
    
    def __init__(self, nombre, fundado, clientes, productos):
        self.nombre = nombre
        self.fundado = fundado
        self.clientes = clientes
        self.productos = productos
        
        
    
    def mostrarGimnasio(self):
        info = f"Nombre del gimnasio: {self.nombre}\nFundado en el año: {self.fundado}\n"
        
        info += "\nCLIENTES DISPONIBLES:\n"
        for cliente in self.clientes:
            info += cliente.mostrarCliente() + "\n"
            
        info += "\nPRODUCTOS DISPONIBLES:\n"
        for producto in self.productos:
            info += producto.mostrarProducto() + "\n"
                
        return info.strip()
      
    def guardarInfo(self):
        opcion = input("Elija el formato para guardar la información (1: TXT, 2: JSON): ")
    
        try:
            if opcion == '1':
                with open('gimnasio.txt', 'w') as file:
                    file.write(self.mostrarGimnasio())
                print("Información guardada en 'gimnasio.txt'.\n")
    
            elif opcion == '2':
                datos = {
                    'Nombre': self.nombre,
                    'Fundado': self.fundado,
                    'Clientes': [cliente.to_dict() for cliente in self.clientes],
                    'Productos': [producto.to_dict() for producto in self.productos]
                }
                with open('gimnasio.json', 'w') as file:
                    json.dump(datos, file, indent = 4)
                print("Información guardada en 'gimnasio.json'.\n")
    
            else:
                print("Opción no válida. Por favor, elija 1 o 2.\n")
        except Exception as e:
            print(f"Se produjo un error al guardar la información: {e}\n")
            
        
    def añadirCliente(self, clientes):
        nombre = input("¿Cuál es el nombre del cliente?\n")
        dni = input("¿Cuál es el DNI del cliente?\n")
        
        # Convertimos saldoCuenta a float para manejar números
        saldoCuenta = float(input("¿Cuánto saldo tiene el cliente en su cuenta?\n"))
    
        # Preguntamos si quiere confirmar la creación del cliente
        eleccion = input(f"Se añadirá un cliente con los siguientes datos:\nNombre: {nombre}\nDNI: {dni}\nSaldo: {saldoCuenta}\n¿Quiere confirmar (y/n)? ").lower()
        print()
        
        if eleccion in ["y", "yes"]:
            clientes.append(Cliente(nombre, dni, saldoCuenta))
            print("Cliente añadido con éxito.\n")
            print()
            
        elif eleccion in ["n", "no"]:
            # Preguntar qué dato se desea cambiar
            dato = input("¿Qué dato quiere cambiar? (Nombre, DNI, Saldo)\n").lower()
    
            if dato == "nombre":
                nombre = input("Introduzca el nuevo nombre\n")
            elif dato == "dni":
                dni = input("Introduzca el nuevo DNI\n")
            elif dato == "saldo":
                saldoCuenta = float(input("Introduzca el nuevo saldo\n"))
            else:
                print("Opción inválida, cancelando creación del cliente.\n")
                print()
                return
    
            # Confirmar de nuevo tras cambiar el dato
            eleccion = input(f"Se añadirá un cliente con los siguientes datos actualizados:\nNombre: {nombre}\nDNI: {dni}\nSaldo: {saldoCuenta}\n¿Quiere confirmar (y/n)? ").lower()
            print()
            
            if eleccion in ["y", "yes"]:
                clientes.append(Cliente(nombre, dni, saldoCuenta))
                print("Cliente añadido con éxito.")
                print()
            else:
                print("Se ha cancelado la creación del cliente.\n")
                print()
        else:
            print("Opción inválida, se ha cancelado la creación del cliente.\n")
            print()
            
    
    
    def añadirProducto(self, productos):
        eleccion = int(input("¿Que tipo de producto quiere añadir?\n1. Proteina\n2. Creatina\n"))
        if eleccion == 1:
            idprod = int(input("¿Cuál es el ID del producto?\n"))
            marca = input("¿Cuál es la marca del producto?\n")
            tipo = input("¿De qué tipo es el producto?\n")
            peso = input("¿Cuál es el peso neto del producto?\n")
            pureza = input("¿Cuál es el porcentaje de pureza del producto?\n")
            sabor = input("¿Cuál es el sabor del producto?\n")
            precio = input("¿Cuánto cuesta?\n")
        
            # Preguntamos si quiere confirmar la creación del cliente
            eleccion = input(f"Se añadirá un producto(Proteína) con los siguientes datos:\nID: {idprod}\nMarca: {marca}\nTipo: {tipo}\nPeso: {peso}Kg\nPureza: {pureza}%\nSabor: {sabor}\nPrecio: {precio}€\n¿Quiere confirmar (y/n)? ").lower()
            print()
            
            if eleccion in ["y", "yes"]:
                productos.append(Proteina(idprod, marca, tipo, peso, pureza, sabor, precio))
                print("Proteína añadida con éxito.\n")
                print()
                
            elif eleccion in ["n", "no"]:
                # Preguntar qué dato se desea cambiar
                dato = input("¿Qué dato quiere cambiar? (ID, Marca, tipo, peso, pureza, sabor, precio)\n").lower()
                
                if dato == "id":
                    idprod = int(input("Introduce el nuevo ID del producto\n"))
                    print()
                if dato == "marca":
                    marca = input("Introduzca la nueva marca del producto\n")
                    print()
                elif dato == "tipo":
                    tipo = input("Introduzca el nuevo tipo de producto\n")
                    print()
                elif dato == "peso":
                    peso = input("Introduzca el nuevo peso\n")
                    print()
                elif dato == "pureza":
                    pureza = input("Introduzca el nuevo porcentaje de pureza\n")
                    print()
                elif dato == "sabor":
                    sabor = input("Introduzca el nuevo sabor\n")
                    print()
                elif dato == "precio":
                    precio = float(input("Introduzca el nuevo precio\n"))
                    print()
                else:
                    print("Opción inválida, cancelando creación del producto.\n")
                    print()
                    return
        
                # Confirmar de nuevo tras cambiar el dato
                eleccion = input(f"Se añadirá un producto(Proteína) con los siguientes datos:\nID: {idprod}\nMarca: {marca}\nTipo: {tipo}\nPeso: {peso}KG\nPureza: {pureza}%\nSabor: {sabor}\nPrecio: {precio}€\n¿Quiere confirmar (y/n)? ").lower()
                print()
                if eleccion in ["y", "yes"]:
                    productos.append(Proteina(idprod, marca, tipo, peso, pureza, sabor, precio))
                    print("Proteína añadida con éxito.")
                    print()
                else:
                    print("Se ha cancelado la creación del producto.\n")
                    print()
            else:
                print("Opción inválida, se ha cancelado la creación del producto.\n")
                print()
                
        
        elif eleccion == 2:
            idprod = int(input("¿Cuál es el ID del producto?\n"))
            marca = input("¿Cuál es la marca del producto?\n")
            tipo = input("¿De qué tipo es el producto?\n")
            peso = input("¿Cuál es el peso neto del producto en KG?\n")
            pureza = input("¿Cuál es el porcentaje de pureza del producto?\n")
            sabor = input("¿Cuál es el sabor del producto?\n")
            precio = input("¿Cuánto cuesta?\n")
            dosisMax = input("¿Cuál es la dosis diaria máxima recomendada en gramos?\n")
            
            # Preguntamos si quiere confirmar la creación del cliente
            eleccion = input(f"Se añadirá un producto(Creatina) con los siguientes datos:\nID: {idprod}\nMarca: {marca}\nTipo: {tipo}\nPeso: {peso}KG\nPureza: {pureza}%\nSabor: {sabor}\nPrecio: {precio}€\nDosis máxima recomendada: {dosisMax}g\n¿Quiere confirmar (y/n)? ").lower()
            print()
            if eleccion in ["y", "yes"]:
                productos.append(Creatina(idprod, marca, tipo, peso, pureza, sabor, precio, dosisMax))
                print("Creatina añadida con éxito.\n")
                print()
            elif eleccion in ["n", "no"]:
                # Preguntar qué dato se desea cambiar
                dato = input("¿Qué dato quiere cambiar? (ID, marca, tipo, peso, pureza, sabor, precio, dosisMax)\n").lower()
        
                if dato == "id":
                    idprod = int(input("Introduce el nuevo ID del producto"))
                    print()
                if dato == "marca":
                    marca = input("Introduzca la nueva marca del producto\n\n")
                    print()
                elif dato == "tipo":
                    tipo = input("Introduzca el nuevo tipo de producto\n\n")
                    print()
                elif dato == "peso":
                    peso = input("Introduzca el nuevo peso en KG\n\n")
                    print()
                elif dato == "pureza":
                    pureza = input("Introduzca el nuevo porcentaje de pureza\n")
                    print()
                elif dato == "sabor":
                    sabor = input("Introduzca el nuevo sabor\n")
                    print()
                elif dato == "precio":
                    precio = float(input("Introduzca el nuevo precio\n"))
                    print()
                elif dato == "dosismax":
                    precio = float(input("Introduzca la nueva dosis máxima\n"))
                    print()
                else:
                    print("Opción inválida, cancelando creación del producto.\n")
                    print()
                    return
        
                # Confirmar de nuevo tras cambiar el dato
                eleccion = input(f"Se añadirá un producto(Creatina) con los siguientes datos:\nID: {idprod}\nMarca: {marca}\nTipo: {tipo}\nPeso: {peso}KG\nPureza: {pureza}%\nSabor: {sabor}\nPrecio: {precio}€\nDosis máxima diaria: {dosisMax}g\n¿Quiere confirmar (y/n)? ").lower()
                print()
                if eleccion in ["y", "yes"]:
                    productos.append(Creatina(idprod, marca, tipo, peso, pureza, sabor, precio, dosisMax))
                    print("Creatina añadida con éxito.")
                    print()
                else:
                    print("Se ha cancelado la creación del producto.\n")
                    print()
            else:
                print("Opción inválida, se ha cancelado la creación del producto.\n")
                print()
        else:
            print("Opción inválida")
            print()
            
        
    def borrarCliente(self, clientes):      
        print("Clientes disponibles:\n\n")
        for cliente in self.clientes:
            cliente.mostrarCliente()
            
        dni = input("Introduce el DNI del cliente que deseas borrar: ")
        
        for cliente in clientes:
            if cliente.dni.lower() == dni.lower():
                clientes.remove(cliente)
                print(f"El cliente con DNI: {cliente.dni} ha sido borrado correctamente.\n")
                return  # Salir después de borrar el cliente
        
        print("No se ha encontrado al cliente con DNI: {dni}")
            

    
    def borrarProducto(self, productos) :
        print("Productos disponibles:\n\n")
        for producto in self.productos:
            producto.mostrarProducto()
            
        idprod = input("Introduce el ID del producto que deseas borrar: ")
        
        for producto in productos:
            if producto.idprod == idprod:
                productos.remove(producto)
                print(f"El producto con ID: {producto.idprod} ha sido borrado correctamente.\n")
                return  # Salir después de borrar el cliente
        
        print("No se ha encontrado el producto con ID: {idprod}")
        
    
    def modificarCliente(self, clientes):
        
        print("Clientes disponibles:\n")
        for cliente in self.clientes:
            cliente.mostrarCliente()
        
        dni = input("Introduce el DNI del cliente que deseas modificar: ")
        
        for cliente in self.clientes:
            if cliente.dni == dni:
                print(f"Cliente encontrado:\n") 
                cliente.mostrarCliente()
                print()
                while True:
                    campo = input("¿Qué campo deseas modificar? (nombre, dni, saldo) o escribe 'salir' para terminar la modificación: ").lower()
                    
                    if campo == "nombre":
                        nuevo_nombre = input(f"Nombre actual: {cliente.nombre}, introduce el nuevo nombre:\n")
                        cliente.nombre = nuevo_nombre
                        print("Nombre actualizado.")
                    
                    elif campo == "dni":
                        nuevo_dni = input(f"DNI actual: {cliente.dni}, introduce el nuevo DNI:\n")
                        cliente.dni = nuevo_dni
                        print("DNI actualizado.")
                    
                    elif campo == "saldo":
                        while True:
                            try:
                                nuevo_saldo = float(input(f"Saldo actual: {cliente.saldoCuenta}, introduce el nuevo saldo:\n"))
                                cliente.saldoCuenta = nuevo_saldo
                                print("Saldo actualizado.")
                                break
                            except ValueError:
                                print("Por favor, introduce un número válido para el saldo.")
                    
                    elif campo == "salir":
                        print("Modificación terminada.")
                        return
                    
                    else:
                        print("Campo no válido. Por favor, elige nombre, dni, saldo o salir.")
                return  # Salir después de modificar el cliente
                
        print("El cliente con DNI: {dni} no se encontró.")
        


    def modificarProducto(self, productos):
        
        print("Productos disponibles:\n")
        for producto in self.productos:
            producto.mostrarProducto()
        
        idprod = int(input("Introduce el ID del producto que deseas modificar: "))
        
        for producto in self.productos:
            if producto.idprod == idprod:
                print(f"Producto encontrado:\n") 
                producto.mostrarProducto()
                if isinstance(producto, Proteina):
                    print()
                    while True:
                        campo = input("¿Qué campo deseas modificar? (ID, marca, tipo, peso, pureza, sabor, precio) o escribe 'salir' para terminar la modificación: ").lower()
                        
                        if campo == "marca":
                            nueva_marca = input(f"Marca actual: {producto.marca}, introduce la nueva marca:\n")
                            producto.marca = nueva_marca
                            print("Nombre actualizado.")
                        
                        elif campo == "tipo":
                            nuevo_tipo = input(f"Tipo actual: {producto.tipo}, introduce el nuevo tipo:\n")
                            producto.tipo = nuevo_tipo
                            print("Tipo actualizado.")
                            
                        elif campo == "pureza":
                            nueva_pureza = input(f"Porcentaje de pureza actual: {producto.pureza}, introduce el nuevo porcentaje de pureza:\n")
                            producto.pureza = nueva_pureza
                            print("Porcentaje de pureza actualizado.")
                            
                        elif campo == "sabor":
                            nuevo_sabor = input(f"Sabor actual: {producto.sabor}, introduce el nuevo sabor:\n")
                            producto.sabor = nuevo_sabor
                            print("Sabor actualizado.")
                            
                        elif campo == "precio":
                            while True:
                                try:
                                    nuevo_precio = float(input(f"Precio actual: {producto.precio}, introduce el nuevo precio:\n"))
                                    producto.precio = nuevo_precio
                                    print("Precio actualizado.")
                                    break
                                except ValueError:
                                    print("Por favor, introduce un número válido para el precio del producto.\n")
                        
                        elif campo == "id":
                            while True:
                                try:
                                    nuevo_id = int(input(f"ID actual: {producto.idprod}, introduce el nuevo ID:\n"))
                                    producto.idprod = nuevo_id
                                    print("ID actualizado.")
                                    break
                                except ValueError:
                                    print("Por favor, introduce un número válido para el ID del producto.\n")
                        
                        elif campo == "peso":
                            while True:
                                try:
                                    nuevo_peso = float(input(f"Peso actual: {producto.peso}, introduce el nuevo peso:\n"))
                                    producto.peso = nuevo_peso
                                    print("Peso actualizado.")
                                    break
                                except ValueError:
                                    print("Por favor, introduce un número válido para el peso del producto.\n")
                        
                        elif campo == "salir":
                            print("Modificación terminada.")
                            print()
                            return
                        
                        else:
                            print("Campo no válido. Por favor, elige nombre, dni, saldo o salir.")
                            print()
                    return  # Salir después de modificar el cliente
                
                elif isinstance(producto, Creatina):
                    print()
                    while True:
                        campo = input("¿Qué campo deseas modificar? (ID, marca, tipo, peso, pureza, sabor, precio, dosisMax) o escribe 'salir' para terminar la modificación: ").lower()
                        
                        if campo == "marca":
                            nueva_marca = input(f"Marca actual: {producto.marca}, introduce la nueva marca:\n")
                            producto.marca = nueva_marca
                            print("Nombre actualizado.")
                        
                        elif campo == "tipo":
                            nuevo_tipo = input(f"Tipo actual: {producto.tipo}, introduce el nuevo tipo:\n")
                            producto.tipo = nuevo_tipo
                            print("Tipo actualizado.")
                            
                        elif campo == "pureza":
                            nueva_pureza = input(f"Porcentaje de pureza actual: {producto.pureza}, introduce el nuevo porcentaje de pureza:\n")
                            producto.pureza = nueva_pureza
                            print("Porcentaje de pureza actualizado.")
                            
                        elif campo == "sabor":
                            nuevo_sabor = input(f"Sabor actual: {producto.sabor}, introduce el nuevo sabor:\n")
                            producto.sabor = nuevo_sabor
                            print("Sabor actualizado.")
                            
                        elif campo == "precio":
                            while True:
                                try:
                                    nuevo_precio = float(input(f"Precio actual: {producto.precio}, introduce el nuevo precio:\n"))
                                    producto.precio = nuevo_precio
                                    print("Precio actualizado.")
                                    break
                                except ValueError:
                                    print("Por favor, introduce un número válido para el precio del producto.\n")
                                    
                        elif campo == "dosismax":
                            while True:
                                try:
                                    nueva_dosis = float(input(f"Dosis diaria máxima recomendada actual: {producto.dosisMax}, introduce la nueva dosis recomendada:\n"))
                                    producto.nueva_dosis = nueva_dosis
                                    print("Dosis actualizada.")
                                    break
                                except ValueError:
                                    print("Por favor, introduce un número válido para la dosis recomendada del producto.\n")
                        
                        elif campo == "id":
                            while True:
                                try:
                                    nuevo_id = int(input(f"ID actual: {producto.idprod}, introduce el nuevo ID:\n"))
                                    producto.idprod = nuevo_id
                                    print("ID actualizado.")
                                    break
                                except ValueError:
                                    print("Por favor, introduce un número válido para el ID del producto.")
                        
                        elif campo == "peso":
                            while True:
                                try:
                                    nuevo_peso = float(input(f"Peso actual: {producto.peso}, introduce el nuevo peso:\n"))
                                    producto.peso = nuevo_peso
                                    print("Peso actualizado.")
                                    break
                                except ValueError:
                                    print("Por favor, introduce un número válido para el peso del producto.")
                        
                        elif campo == "salir":
                            print("Modificación terminada.")
                            print()
                            return
                        
                        else:
                            print("Campo no válido. Por favor, elige nombre, dni, saldo o salir.")
                            print()
                    return  # Salir después de modificar el cliente
        print("El cliente con DNI: {dni} no se encontró.")
        print()


