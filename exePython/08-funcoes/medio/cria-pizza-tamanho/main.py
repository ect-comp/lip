def criaPizza (pizza, x):
	nova = []
	for ing in pizza:
		n = len(ing)
		if n >= x or n % 2 == 0:
			nova.append(ing)
			
	return nova

n = int(input())
x = int(input())

pizza1 = []

for i in range(n):
	pizza1.append(input())
	
pizza2 = criaPizza(pizza1, x)

print(f"Pizza original: {pizza1}")
print(f"Pizza nova: {pizza2}")
