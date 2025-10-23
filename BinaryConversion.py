# Program to convert decimal to binary, octal, and hexadecimal

decimal = int(input("Enter a decimal number: "))

# Convert and print the values
print("Binary:", bin(decimal)[2:])   # [2:] removes '0b' prefix
print("Octal:", oct(decimal)[2:])     # [2:] removes '0o' prefix
print("Hexadecimal:", hex(decimal)[2:].upper())  # [2:] removes '0x' prefix, .upper() makes it uppercase
