class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


usr_input = input('divide')

try:
    x, y = int(usr_input.split('/')[0]), int(usr_input.split('/')[1])
    if y == 0:
        raise DivisionByZero('thou shalt not divide by zero')
except (ValueError, DivisionByZero) as err:
    print(err)
else:
    print(x/y)
