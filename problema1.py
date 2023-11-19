def sumar_5_enteros():
    lista = []
    contadorwhile = 0
    tamaño = 5
    suma = 0

    while contadorwhile < tamaño:
        lista.append(int(input("ingrese numero"+str(contadorwhile+1) +": ")))
        contadorwhile +=1

    while contadorwhile < tamaño:
        suma+= lista[contadorwhile]
        contadorwhile +=1
    print("los elementos de la lista son:")
    for numero in lista:
        print(numero,end=', ')
    print("\nla suma de todos sus elementos es:")
    print(suma)



