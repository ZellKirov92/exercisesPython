import json
# 1. Lecture du fichier 
with open('./user.json') as f:
    user_data = f.read()
    user_json_dict = json.loads(user_data)
print(user_json_dict)
# 2. Afficher l'age 
print(f' Age : {user_json_dict['age']}')
# 3. Afficher le second hobbies
print(f'Le second hobby est : {user_json_dict['hobbies'][1]}')
# 4. Afficher l'email 
print(f'l\'email de l\'utilisateur est : {user_json_dict['email']}')