user_number = int(input('Veuillez entrer un nombre : '))
table = []
for i in range(1, 11):
    if (user_number * i) % 3 == 0:
        table.append(f'{user_number * i}*')
    else:
        table.append(user_number * i)
    
print(table)