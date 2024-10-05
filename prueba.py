def ejercicioDelCambio():
    # Ingresar el valor del cambio que se quiere dar
    valor_cambio = int(input("Ingrese el valor del cambio: "))

    # Ingresar la cantidad de monedas disponibles
    cantidad_monedas = int(input("Ingrese la cantidad de monedas disponibles: "))

    # Ingresar los valores de las monedas y almacenarlas en el conjunto C
    C = []
    print("Ingrese los valores de las monedas:")
    for i in range(cantidad_monedas):
        valor_moneda = int(input(f"Valor de la moneda {i + 1}: "))

        # Verificar si la moneda ya existe en el conjunto C
        if valor_moneda in C:
            input("No se puede agregar el mismo valor de moneda más de una vez. PROGRAMA FINALIZADO. Presiona Enter para terminar.")
            exit()  # Termina el programa si se encuentra un valor repetido
        else:
            C.append(valor_moneda)  # Agregar la moneda al conjunto si no está repetida

    # Ordenar el conjunto de monedas de mayor a menor
    C.sort(reverse=True)

    # Calcular el conjunto solución S usando un algoritmo voraz
    S = []
    restante = valor_cambio
    for moneda in C:
        if moneda <= restante:  # Si la moneda es menor o igual a lo que queda del cambio
            S.append(moneda)  # Añadir la moneda al conjunto solución
            restante -= moneda  # Restar el valor de la moneda al cambio restante

    # Verificar si se pudo dar el cambio exacto
    if restante == 0:
        # Mostrar los conjuntos C y S solo si se puede dar el cambio exacto
        print("\nConjunto C (valores de las monedas disponibles):", C)
        print("Conjunto S (solución con las monedas elegidas):", S)
    else:
        print(f"No se puede dar el cambio exacto de {valor_cambio} con las monedas disponibles.")


def ejercicioLexicografico():
    # Ingresar la palabra completa
    palabra = input("Ingrese una palabra: ")

    # Convertir la palabra a una lista de caracteres
    caracteres = list(palabra)

    # Inicializar la solución como una cadena vacía
    solucion = ""

    # Algoritmo voraz: Seleccionar el carácter más grande en cada paso
    while caracteres:
        # Seleccionar el mayor carácter disponible
        max_char = max(caracteres)
        # Añadirlo a la solución
        solucion += max_char
        # Eliminarlo de la lista de caracteres
        caracteres.remove(max_char)

    # Mostrar el resultado
    print("La palabra ordenada lexicográficamente de mayor a menor es:", solucion)

# ejercicioDelCambio()
ejercicioLexicografico()