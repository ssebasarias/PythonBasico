# Operaciones en diccionarios
# .keys():Retorna la clave de nuestro elemento.

# .values(): Retorna una lista de elementos (valores del diccionario).

# .items(): Devuelve lista de tuplas (primero la clave y luego el valor).

# .clear(): Elimina todos los items del diccionario.

# .pop(“n”): Elimina el elemento ingresado.

# Cómo trabajar con diccionarios
# Definir función principal
def run():
    # Defino el diccionario, agrego los valores.
    mi_diccionario = {
      'llave1' : 1,
      'llave2' : 2,
      'llave3' : 3,
    }

# Imprimir las llaves del diccionario utilizando un bucle for. Con ‘.keys()’ estamos llamando a imprimir las llaves, no los valores.
    for llave in mi_diccionario.keys():
        print(llave)

# Imprimir los valores del diccionario empleando un bucle for. Con ‘.values()’ estoy llamando a imprimir los valores.
    for valores in mi_diccionario.values():
        print(valores)

# Imprimir las llaves y los valores usando ‘.items()’. Para esto, coloco las variables llave e items.
    for llave, items in mi_diccionario.items():
        print("La llave: '" + llave + "' contiene el item: " + str(items))

if __name__ == '__main__':
    run()