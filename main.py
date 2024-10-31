import FuncionesPrincipales as prin
# Bucle principal
while True:
    opcion = int(input(f"Bienvenido a {prin.miGym.nombre}, ¿es usted administrador(1) o usuario(2)? Pulse (3) si desea salir del programa\n"))
    
    match opcion:
        case 1:
            prin.gestionar_admin()
        case 2:
            prin.gestionar_usuario()
        case 3:
            print("Saliendo...\n")
            break