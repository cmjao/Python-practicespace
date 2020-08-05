class Thing():
    pass

example = Thing()

print(example)

class Thing2():
    letters = 'abc'

print(Thing2.letters)

class Thing3():
    def __init__(self):
        self.letters = 'xyz'

thing3 = Thing3()

print(thing3.letters)