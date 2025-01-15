import math

# Variables globales
baraja = []
lista1 = []
lista2 = []
lista3 = []
cartaElegida = None
posicionCartaElegida = 0
repeticiones = 0
cartasCorrectas = False

def agregarCarta(numero):
    baraja.append(numero)

def obtenerNumeroCartas(datosPantalla):
    global numeroCartas, repeticiones, posicionCartaElegida, cartasCorrectas
    if int(datosPantalla) % 3 != 0 or int(datosPantalla) > 81:
        print("Error: Ingrese un multiplo de tres entre 0 y 81")
        cartasCorrectas = False
    else:
        numeroCartas = int(datosPantalla)
        if numeroCartas == 3:
            repeticiones = 1
        elif 3 < numeroCartas <= 9:
            repeticiones = 2
        elif 9 < numeroCartas <= 27:
            repeticiones = 3
        elif 27 < numeroCartas <= 81:
            repeticiones = 4
        posicionCartaElegida = math.ceil((numeroCartas + 1) / 2) - 1
        cartasCorrectas = True

def ordenarListas(numeroListaMedio):
    global cartaElegida
    if numeroListaMedio == 1:
        baraja.extend(lista2)
        baraja.extend(lista1)
        baraja.extend(lista3)
    elif numeroListaMedio == 2:
        baraja.extend(lista1)
        baraja.extend(lista2)
        baraja.extend(lista3)
    elif numeroListaMedio == 3:
        baraja.extend(lista1)
        baraja.extend(lista3)
        baraja.extend(lista2)
    lista1.clear()
    lista2.clear()
    lista3.clear()
    cartaElegida = baraja[posicionCartaElegida]

def llenar_grupos():
    for i in range(len(baraja) // 3):
        lista1.append(baraja.pop(0))
        lista2.append(baraja.pop(0))
        lista3.append(baraja.pop(0))
    print("lista 1:", lista1)
    print("lista 2:", lista2)
    print("lista 3:", lista3)

def elegir_lista():
    lista_elegida = int(input("¿En qué grupo está tu carta? (1, 2, o 3): "))
    ordenarListas(lista_elegida)

def imprimir_grupos():
    print("Lista 1:", lista1)
    print("Lista 2:", lista2)
    print("Lista 3:", lista3)

def iniciar(datosPantalla):
    global cartaElegida
    obtenerNumeroCartas(datosPantalla)
    if cartasCorrectas:
        baraja.clear()
        for i in range(1, numeroCartas + 1):
            agregarCarta(i)
        print("Elige una carta mentalmente.")
        llenar_grupos()
        for _ in range(repeticiones):
            imprimir_grupos()
            elegir_lista()
            llenar_grupos()
        print("Elegiste la carta #", cartaElegida)


datos = input("¿Cuantas cartas quieres jugar (3, 9, 27, o 81)? ")
iniciar(datos)