speed_kmh = float(input('Veuillez entrer une vitesse en km/h : '))
kmh_to_mph = 1.609
speed_mph = speed_kmh / kmh_to_mph

print(f'{speed_kmh} km/h = {speed_mph} m/h')
# arrondir le resultat au centième près
print(f'{speed_kmh} km/h = {round(speed_mph, 2)} m/h')