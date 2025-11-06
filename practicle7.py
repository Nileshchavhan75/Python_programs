# Convert Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))  
fahrenheit = (celsius * 9/5) + 32  
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

# Convert Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))  
celsius = (fahrenheit - 32) * 5/9  
print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
