n = int(input())

l1 = []
for i in range(n):
	l1.append(input())

l2 = []
for i in range(n):
	l2.append(input())

for time1 in l1:
	time2 = l2.pop()
	print(f"{time1} x {time2}")

