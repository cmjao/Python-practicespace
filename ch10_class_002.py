class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print(self.name, self.symbol, self.number)
    def __str__(self):
        return ('%s %s %s' % (self.name, self.symbol, self.number))
    @property
    def get_name(self):
        return self.name
    @property
    def get_symbol(self):
        return self.symbol
    @property
    def get_number(self):
        return self.number

e = Element('Hydrogen', 'H', 1)

hydrogen_dict = {'name':'Hydrogen', 'symbol':'H', 'number':1}
hydrogen = Element(hydrogen_dict['name'],hydrogen_dict['symbol'],hydrogen_dict['number'])
e.dump()
print(hydrogen)
print(hydrogen.get_name, hydrogen.get_symbol, hydrogen.get_number)