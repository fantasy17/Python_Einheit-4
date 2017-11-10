f = open("phonebook.txt", "r")
xs = f.readlines()
f.close()

xs.sort()
print(xs)
print(len(xs))

xs.append("John: 876\n")
xs.sort()

g = open("sorted.txt", "w")
for v in xs:
	g.write(v)
g.close()

for i in xs:
	name, number = i.split(": ")
	print(name)
	print(number)
#look at pictures