n = int(input())
l1 = []
for i in range(n):
	l1.append(input())

x = int(input())
y = int(input())

l2 = []
for elemento in l1:
	if len(elemento) != x and len(elemento) != y:
		l2.append(elemento)

print(l2)
