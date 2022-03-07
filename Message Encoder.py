import random

text = input("Enter a character or strings to convert into ascii values: ")
ascii_values = []
new_values = []
second_multiples = []
for character in text:
    ascii_values.append(ord(character))
print(f'The ascii values are {ascii_values}')

random_integer = random.randrange(0, 1000)
print(f'The random number generated is {random_integer}')

if ascii_values[0] == min(ascii_values) and ascii_values[1] == max(ascii_values):
    print(
        f'N1 = {ascii_values[0]} is the lowest permissible value and N2 = {ascii_values[1]} is the highest '
        f'permissible value')
    for i in ascii_values:
        new_values.append(i + random_integer)
    print(f'The new values are {new_values}')
    if random_integer > ascii_values[1]:
        for i in range(1, ascii_values[1]):
            if ascii_values[1] % i == 0:
                second_multiples.append(i)
            else:
                continue
        print(f'The multiples of {ascii_values[1]} are {second_multiples}')
        calc = random_integer - max(second_multiples)
        print(f'Result of subtracting max num of SM from RI is {calc}')
        ascii_values[0] = ascii_values[0] + calc
        print(f'After adding calc to N1 in AV is {ascii_values}')
        print('\n')
        display_char = ascii(ascii_values)
        print(f'The encoded message is {display_char}')
    else:
        print(f'The random integer {random_integer} is less than the ascii_value {ascii_values[1]}')
else:
    print(
        f'N1 = {ascii_values[0]} is not the lowest permissible value or N2 = {ascii_values[1]} is not the highest '
        f'permissible value')