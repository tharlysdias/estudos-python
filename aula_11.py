# Listas === []
a = [1,2,3]
print(type(a))

print(help(list))

print(dir(a))

print(a)
a.append(4)
print(a)

b = a.copy()
print(b)

c = a
print(c)

a.append(1)
print(a)
print(a.count(1))

print(a,b)


b = ["um", "dois", "tres"]
a.extend(b)
print(a)

a = [1,2,3,4]
a.append(b)
print(a)
print(a.index(4))
a.insert(3, "Novo Valor")
print(a)

# Remove o valor da lista e mostra qual o valor será removido
print(a.pop())
print(a)

# Só Remove o valor da lista
a.remove("Novo Valor")
print(a)

# Faz a inversão da ordem
a.reverse()
print(a)

# Faz a reinversão da ordem (volta ao normal)
a.sort()
print(a)

b = ["c","d", "b", "a"]
b.sort()
print(b)

# Limpa minha lista
b.clear()
print(b)


for i in a:
	print(i)


print(a[1])