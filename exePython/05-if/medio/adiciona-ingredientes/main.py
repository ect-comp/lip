todos = input().split(",")
toni = input().split(",")

copia = todos[:]

for ingrediente in toni:
	if ingrediente not in todos: 
		todos.append(ingrediente)

print(copia)
print(todos)
