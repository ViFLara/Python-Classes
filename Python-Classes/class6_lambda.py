counter_letters = lambda list: [len(x) for x in list]

animals_list = ['dog', 'cat', 'elephant']
print(counter_letters(animals_list))

sum = lambda a, b: a + b
print(sum(5, 10))

# dictionary
calculator = {
    'sum': lambda a, b: a + b,
    'subtraction': lambda a, b: a - b,
    'multiplication': lambda a, b: a * b,
    'division': lambda a, b: a / b,
}

print(type(calculator))
sum = calculator['sum']
multiplication = calculator['multiplication']
print("Sum is: {}" .format(sum(10, 4)))
print("Multiplication is: {}" .format(multiplication(10, 2)))
