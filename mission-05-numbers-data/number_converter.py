# Number converter: decimal to binary and hexadecimal

text = input("Enter a positive whole number: ")
number = int(text)

binary = bin(number)[2:]
hexadecimal = hex(number)[2:].upper()

print("Decimal:", number)
print("Binary:", binary)
print("Hexadecimal:", hexadecimal)
