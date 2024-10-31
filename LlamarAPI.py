import requests

def obtener_datos_api():
    # Pide al usuario seleccionar la API
    seleccion = input("Ingresa (1) para obtener ejercicios o (2) para obtener máquinas de gimnasio: ")
    
    # Define la URL según la selección
    if seleccion == "1":
        url = "https://proyectoinicialpython2dam.onrender.com/api/ejercicios"
    elif seleccion == "2":
        url = "https://proyectoinicialpython2dam.onrender.com/api/maquinasGIMNASIO"
    else:
        print("Selección inválida. Por favor, ingresa 1 o 2.")
        return  # Termina la ejecución si la selección no es válida

    try:
        # Realiza la solicitud GET a la URL seleccionada
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Verifica si hubo un error en la respuesta
        datos = respuesta.json()  # Convierte la respuesta a JSON

        # Imprime los datos obtenidos
        if seleccion == "1":
            print("Datos de ejercicios obtenidos de la API:")
            for musculo, ejercicios in datos.get("musculos", {}).items():
                print(f"\nEjercicios para {musculo.capitalize()}:")
                for ejercicio in ejercicios:
                    print(f"- {ejercicio['nombre']} ({ejercicio['tipo']} - Dificultad: {ejercicio['dificultad']})")
                    print(f"  Series: {ejercicio['series']}, Repeticiones: {ejercicio['repeticiones']}")

        elif seleccion == "2":
            print("Datos de máquinas de gimnasio obtenidos de la API:")
            for maquina in datos.get("gimnasio", {}).get("maquinas", []):
                print(f"- {maquina['nombre']} ({maquina['tipo']}) - Grupo muscular: {', '.join(maquina['grupoMuscular'])}")

    except requests.exceptions.RequestException as e:
        print("Error al conectar con la API:", e)

