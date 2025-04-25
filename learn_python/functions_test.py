def print_every_number(*tuple_of_numbers):
    print(type(tuple_of_numbers))
    for arg in tuple_of_numbers:
        print(arg)

print_every_number(1, 2, 2, 3, 3, 4, 5, 5)







def greeting(name: str):
    print("Hello, my name is " + name)

#greeting(24601)



# -> float will ensure a float is given as the type hint
def division(numerator: int = 5, denominator: int = 2) -> float:
    return numerator / denominator


a: int = 4
b: int = 6
print(division(a, b))
