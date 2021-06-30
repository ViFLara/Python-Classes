class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


while True:
    try:
        x = int(input('Enter a grade from 0 to 10'))
        print(x)
        if x > 10:
            raise InputError('Grade can not be upper then 10')
        elif x < 0:
            raise InputError('Grade can not be lower then 0')
        break
    except ValueError:
        print('Invalid Value. Enter only numbers.')
    except InputError as ex:
        print(ex)


class InputError(Exception):
    def __init__(self, message):
        self.message = message

nome = 'Adda'
while True:
    try:
        x = input('Digite um nome: ')
        if x == nome:
            break
        else:
            raise InputError('Nome inválido')
    except InputError as ex:
        print(ex)