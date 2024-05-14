import random

level = int(input('veuillez choisir un niveau de difficulté : Facile /1, Moyen / 2, Difficile / 3 : '))
max = 100
if level == 1:
    max = 10
elif level == 2:
    max = 100
elif level == 3:
    max = 1000
secret_number = random.randint(0, max)
user_number = int(input(f'veuillez entrer un nombre entre 0 et {max} : '))
attempts = 1
while secret_number != user_number:
    if user_number > secret_number:
        print(f'le nombre est plus petit que {user_number}')
    else:
        print(f'le nombre est plus grand que {user_number}')
    
    user_number = int(input('veuillez entrer un nombre entre 0 et 100 : '))
    attempts += 1
    
print(f'Bravo, vous avez trouver le nombre {secret_number} en {attempts} tentatives')
    