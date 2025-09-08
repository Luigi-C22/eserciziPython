#I metodi delle stringhe

random_alnum = "dsaljoiajd8rgkrjvnklr7r34dw"
match = "d"
counter = 0

for char in random_alnum:
    if char == match:
        counter += 1

output = f"hot trovato {counter} caratteri '{match}'"

print(output)
