n = int(input())

l1 = list(range(2, n, 2))

v1 = int(input())
v2 = int(input())

l2 = l1[:]
l2.pop(v1)
l2.pop(v2)

print(l1)
print(l2)
