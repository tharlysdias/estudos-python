# Funções - parte 1
def calcula_dobro(numero):
    total = numero * 2
    return total

resultado = calcula_dobro(8)

print(resultado)


# Funções - Argumentos unidimensionais, bidimensionais
# Exemplo 1
def calcula_soma_numeros(numero1, numero2, numero3):
    total = numero1 + numero2 + numero3
    return total

soma = calcula_soma_numeros(2,3,4)
print("O resultado da soma é %d" % soma)

# Exemplo 2
def calcula_suma_numeros(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

soma = calcula_suma_numeros(2,3,4,5,6,7,8,9)
print("O resultado da soma é %d" % soma)


# Exemplo 3
def calcula_suma_numeros(*numeros):
    return sum(numeros)

soma = calcula_suma_numeros(2,3,4,5,6,7,8,9)
print("O resultado da soma é %d" % soma)


# Exemplo 4
def calcula_suma_numeros(**numeros):
    total = 0
    for item in numeros:
        total += numeros[item]
    return total

soma = calcula_suma_numeros(num1=5, num2=10, num3=20)
print("O resultado da soma é %d" % soma)


# Exemplo 5
def calcula_suma_numeros(**numeros):
    return sum(numeros.values())

soma = calcula_suma_numeros(num1=5, num2=10, num3=20)
print("O resultado da soma é %d" % soma)


# Exemplo 6
def calcula_suma_numeros(num1, num2, **numeros):
    import pdb; pdb.set_trace()
    return sum(numeros.values())

soma = calcula_suma_numeros(num1=5, num2=10, num3=20, num4=7, num5=90)
print("O resultado da soma é %d" % soma)


# Exemplo 7
def calcula_suma_numeros(**numeros):
    for item in numeros:
        import pdb; pdb.set_trace() #break point
    return sum(numeros)

soma = calcula_suma_numeros(num1=5, num2=10, num3=20)
print("O resultado da soma é %d" % soma)