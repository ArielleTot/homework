print('2) Decimal to binary')
decimal = int(input())
binary = bin(decimal)[2:].zfill (8)
print(binary)

print('3) Hex to ASCII')
message_list = input('Gimme an input')
message_list = message_list.split(' ')
message_list = list([int(a, 16) for a in message_list])
my_string = ''
for character in message_list:
    my_string +=(chr(character))
print(my_string)

print('4) Binary to hex, no spaces')
binary = int(input(), 2)
hexa = hex(binary)
print(hexa)

print('5) Octal to decimal')
def my_function(number):
    return int(str(number), 8)
print (my_function(input('octal number: ')))
