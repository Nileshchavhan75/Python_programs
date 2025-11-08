# tuple = ("Nilesh", 12, 78.8, "Chavhan", [10 , 20, 30])

# print(tuple[0])
# print(tuple[4])

# tuple = (10,20,10,20,40,10,50,20,60)
# print(tuple.count(10))

# tuple = ("Nilesh","Rutuja","Shivay","Niru")
# print(tuple.index("Niru"))


tuple1 = ("Nilesh","Rutuja","Shivay","Niru")
print(tuple1)
my_list = list(tuple1)
print(my_list)
my_list[1] = "Rutu"

my_tuple = tuple(my_list)

print(my_list)
print(my_tuple)