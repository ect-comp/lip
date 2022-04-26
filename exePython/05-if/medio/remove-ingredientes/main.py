todos = input().split()
toni = input().split()

copia = todos[:]

for ingrediente in toni:
	if ingrediente in todos: 
		todos.remove(ingrediente)

print(copia)
print(todos)

