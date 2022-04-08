n = int(input())

l1 = list(range(1, n + 1))

v1 = int(input())
v2 = int(input())

l2 = l1[:]

l1.remove(v1)
l1.remove(v2)

print(l1)
print(l2)
