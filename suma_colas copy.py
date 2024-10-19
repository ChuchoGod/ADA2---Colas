import queue

cola1 = queue.Queue()
cola2 = queue.Queue()
cola3 = queue.Queue()
rango = int(input("Dame el rango de las colas:"))

for i in range(rango):
    dat1 = int(input(f"Dame el dato #{i+1} de la cola 1:"))
    cola1.put(dat1)

for i in range(rango):
    dat2 = int(input(f"Dame el dato #{i+1} de la cola 2:"))
    cola2.put(dat2)

for i in range(rango):
    valor1 = cola1.get()
    valor2 = cola2.get()
    suma = valor1 + valor2
    cola3.put(suma)

    print(f"Iteración {i+1}:")
    print(f"  Valor desencolado de cola 1: {valor1}")
    print(f"  Valor desencolado de cola 2: {valor2}")
    print(f"  Cola 1 ahora: {[cola1.queue[i] for i in range(cola1.qsize())]}")
    print(f"  Cola 2 ahora: {[cola2.queue[i] for i in range(cola2.qsize())]}")

resultado = []

while not cola3.empty():
    resultado.append(cola3.get())

print(f"Cola 3: {resultado}")
