list = [1, 10]
file = open('test.txt', 'r')
try:
    text = file.read()
    division = 10 / 1
    number = list[1]
except ZeroDivisionError:
    print('Unable to perform a division by zero')
except ArithmeticError:
    print('There was an error performing an arithmetic operation.')
except IndexError:
    print("Error accessing invalid list index")
except Exception as ex:
    print(f'Unknown error. Error: {ex}')
else:
    print('Run when no exception occurs')
finally:
    print('Always run')
    print('Closing file')
    file.close()
