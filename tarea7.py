import math

def area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

radio = 3
resultado = area_circulo(radio)
print("El área del círculo con radio", radio, "es:", resultado)
