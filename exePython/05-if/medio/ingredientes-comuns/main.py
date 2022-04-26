paolo = input().split()
toni = input().split()
dois = []

for ingrediente in toni:
	if ingrediente in paolo: 
		dois.append(ingrediente)
		paolo.remove(ingrediente)
		
print(dois)
print(paolo)
