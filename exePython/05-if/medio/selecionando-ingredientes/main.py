n = int(input())
l1 = []
for i in range(n):
	l1.append(input())

x = int(input())
y = int(input())

l2 = sorted(l1)[x:y+1]

print(l2)
