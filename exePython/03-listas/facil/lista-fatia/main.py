n = int(input())

l1 = list(range(1, n + 1, 2))

v1 = int(input())
v2 = int(input())

l2 = l1[v1:(v2+1)]

print(sum(l2))
