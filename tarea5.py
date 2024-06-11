def contar_mayusculas_minusculas(cadena):
    mayusculas = sum(1 for c in cadena if c.isupper())
    minusculas = sum(1 for c in cadena if c.islower())
    print("Mayúsculas:", mayusculas)
    print("Minúsculas:", minusculas)

texto = "Hola Mundo"
contar_mayusculas_minusculas(texto)
