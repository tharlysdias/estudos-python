# Loop for
# Intera sobre uma lista
# Pode ser qualquer lista (números ou strings)
# Objeto interavel
for i in [1,2,3]:
	print(i)
else:
	print("Fim do loop")

# Contando Strings
for i in "Tharlys Dias":
	print(i)
else:
	print("Fim do loop")

# Função biotina do python que conta de 0 até um determinado número
for i in range(4, 10):
	print(i)
else:
	print("Fim do loop")


list1 = ["Maça", "Banana", "Melao"]
list2 = ["Tomate", "Cebola", "Cenoura"]

# Interando duas listas ao mesmo tempo utilizando zip
for i, j in zip(list1, list2):
	print(i, j)
else:
	print("Fim do loop")


# Função enumerate que retorna um índice de contagem
for i, j in enumerate(list1):
	print(i, j)
else:
	print("Fim do loop")