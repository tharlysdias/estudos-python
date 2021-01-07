# Operadores de atribuição
a = 10


# Python possibilita a declaração de várias variaveis na mesma atribuição, utilizando atribuições diferentes (ao mesmo tempo)
maisIgual, menosIgual, vezesIgual, divididoIgual, moduloIgual = 5,6,7,8,9

print(str(maisIgual) + "-" + str(moduloIgual))

# Operadores de atribuições classicas
maisIgual += 1 #resultado 6
menosIgual -= 1 #resultado 5
vezesIgual *= 1 #resultado 7
divididoIgual /= 1 #resultado 8.0
moduloIgual %= 2 #resultado 1

print(maisIgual, menosIgual, vezesIgual, divididoIgual, moduloIgual)

# Atribuição e calculo ao mesmo tempo
a, b, c = 2,4,8
a, b, c = a*2, a+b+c, a*b*c

print(a,b,c)