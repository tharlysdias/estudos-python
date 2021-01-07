# Loop while
condicao = True
while condicao:
	print("Executou")
	condicao = False
else:
	print("Fim do loop")

# Utilizando continue
i = 0
while i < 10:
	if i == 5:
		i = i + 1
		continue
	print(i)
	i = i + 1
else:
	print("Fim do loop")

# Utilizando break
f = 0
while f < 10:
	if f == 5:
		break
	print(f)
	f = f + 1
else:
	print("Fim do loop")