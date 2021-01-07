# Python é uma linguagem dinamica e forte, que precisa de indentação
class MyClass():
	a = 10
	b = 3
	a + b
	print(a+b)

	if a > b:
		print("a é maior que b")
		a = a - 1
	if b > a:
		print("b é maior que a")
		b = a + 10


	if 1>0:
		a = a - 1
		b = a + 10

		try:
			pass
		except Exception as e:
			raise e


# Declaração de variavel
# Tipos de variaveis
# As variaveis não podem começar com números
a = 10
print(type(a))

# Python sempre vai criar uma nova variavel mesmo tendo o mesmo nome
a = "10"
print(type(a))

b = 10.5
print(type(b))

c = "String"
print(type(c))

d = ["Item 1", "Item 2", "Item 3",]
print(type(d))

e = ("Item 1", "Item 2", "Item 3")
print(type(e))

f = {1: "Fulano", 2: "Ciclano", 3: "Beltrano"}
print(type(f))