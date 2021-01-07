# Dicionários === {}
# d = {key: value}
d = {"nome": "Tharlys", "idade":25}
print(d["idade"])
print(d["nome"])

# Adiciona
d["salario"] = 5000
print(d)

print(dir(d))

# Imprimi os valores contidos no dicionario
print(d.values())

#Imprimi as chaves contidas no dicionario
print(d.keys())

dic2 = {"rua": "Russia", "bairro": "Velha"}
# Atualiza o dicionario 1 com as informações do dicionario 2
d.update(dic2)
print(d)
# Se a chave já existir ela é atualizada
dic2 = {'rua': "Russia", 'bairro': "Velha", 'nome': "Ciclano"}
d.update(dic2)
print(d)


print(d.setdefault("nome", "Não encontrado"))
print(d)

# Retira o item do dicionario
# print(d.popitem())
print(d)

print(d.pop("salario"))
print(d)


print(d.get("nome"))
print(d.get("salario", "404"))


print(help(dict.fromkeys))

print(d.fromkeys([1,2,3], "x"))
print(d)

print(dict.fromkeys([1,2,3], "x"))


d.copy()
print(d)

d.clear()
print(d)


d = {1: "um", 2: "dois"}
print(d)


for i in d:
	print(i)

for i in d.items():
	print(i)


print(d.items())

for i in d.items():
	print(i[1])