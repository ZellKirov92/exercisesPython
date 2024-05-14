first_side = float(input('veuillez entrer la logueur du premier côté : '))
second_side =  float(input('veuillez entrer la logueur du second côté : '))
third_side = float(input('veuillez entrer la longueur du troisième côté : '))

if first_side == second_side == third_side :
    print('Le triangle est Équilatérale')
elif first_side == second_side or first_side == third_side or second_side == third_side:
    print('le triangle est Isocèle')
else: 
    print('le triangle est quelconque')