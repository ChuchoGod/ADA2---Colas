colas = {}
contadores = {}

def agregar_servicio(numero_servicio):
    """Inicializa una cola y un contador para un nuevo servicio."""
    if numero_servicio not in colas:
        colas[numero_servicio] = []
        contadores[numero_servicio] = 0

def llegada_cliente(numero_servicio):
    """Simula la llegada de un cliente."""
    if numero_servicio not in colas:
        agregar_servicio(numero_servicio)

    contadores[numero_servicio] += 1
    numero_atencion = contadores[numero_servicio]
    colas[numero_servicio].append(numero_atencion)
    print(f"Cliente con número {numero_atencion} agregado a la cola del servicio {numero_servicio}")

def atender_cliente(numero_servicio):
    """Atiende al siguiente cliente en la cola."""
    if numero_servicio not in colas or not colas[numero_servicio]:
        print(f"No hay clientes para atender en el servicio {numero_servicio}")
    else:
        numero_atencion = colas[numero_servicio].pop(0)
        print(f"Atendiendo al cliente con número {numero_atencion} del servicio {numero_servicio}")

def procesar_comando(comando):
    """Interpreta y ejecuta el comando ingresado."""
    try:
        accion, numero_servicio = comando[0], int(comando[1:])
        if accion == 'C':
            llegada_cliente(numero_servicio)
        elif accion == 'A':
            atender_cliente(numero_servicio)
        else:
            print("Comando no reconocido. Use 'C' para llegada de cliente o 'A' para atención.")
    except (IndexError, ValueError):
        print("Comando inválido. El formato debe ser 'C' o 'A' seguido de un número de servicio.")

while True:
    comando = input("Ingrese un comando (C para llegada de cliente, A para atención de cliente, o 'salir' para terminar): ")
    if comando.lower() == 'salir':
        break
    procesar_comando(comando)
