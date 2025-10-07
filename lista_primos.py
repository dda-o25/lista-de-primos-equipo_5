"""
El propósito de este programa es que dado un número, el programa calcule una lista de todos los numeros primos antes y si incluye, tambien el numero dado
Eduardo Caleb Castillo Llanas
Daniel Maldonado Delgado
Larisa Carolina Alvarez Gonzales
Ximena Castro Flores
03/Oct/25
"""
# Entradas
numero = int(input("Introduzca un número: "))

# Procesos
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for n in range(1, numero + 1):
    if es_primo(n):
        print(n, end=" ")
