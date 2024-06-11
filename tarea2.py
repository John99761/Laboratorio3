def multiplicar_lista(lista):
 
  producto = 1
  for numero in lista:
      producto *= numero
  return producto


numeros = [1, 2, 3, 4, 5]
resultado = multiplicar_lista(numeros)
print("El producto de los números en la lista es:", resultado)
