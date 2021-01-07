# Tuples or Tuplas === ()
a = 1,2,3,4
print(type(a))
print(a[2])

b = (1,2,3)
print(type(b))
print(b[0])

c = 1,2,3,4,("asdf",2,"a"), 1.2,"asd"
print(type(c))
print(c)
print(c[4])
print(c[4][0])

print(dir(b))

d = (2,2,3,4,"asd", (1,2), "asd")
print(type(d))
print(d.count("asd"))
print(d.count("asdf"))
print(d.index((1,2)))


if d.count("asda"):
	print(d[d.index("asda")])

if d.count("asd"):
	print(d[d.index("asd")])


# Loop (for) com Tuplas
for i in d:
	print(i)


# Loop (while) com Tuplas
i = 0
while i < len(d):
	print(d[i])
	i = i + 1