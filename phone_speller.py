user_numbers = str(input('enter your phone number : '))
digits_mapping1 = {
    '0' : 'Zero',
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
}

digits_mapping2 = {
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Nine'
}
digits_mapping1['4'] = 'Four' 
dictionary = digits_mapping1 | digits_mapping2
print(dictionary)
result = ''
for digit in user_numbers:
    result += dictionary.get(digit, '[character not mapped]') + ' '

print(result)