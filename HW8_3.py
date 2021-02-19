class NotANumber(Exception):
    def __init__(self, msg):
        self.msg = msg


def run():
    res = []
    while True:
        usr_input = input("input ")
        if usr_input == 'quit':
            return res
        try:
            if not usr_input.isnumeric():
                raise NotANumber("something is wrong with your input")
        except NotANumber as err:
            print(err)
        else:
            res.append(int(usr_input))


print(run())
