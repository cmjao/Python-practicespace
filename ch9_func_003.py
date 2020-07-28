# decorator

def test(func):
    def new_func(*args, **kwargs):
        print('start')
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        print('end')
        return result
    return new_func

def add_ints(a, b):
    return a + b

a = test(add_ints)
a(8, 9)

b = test(print)
b('aaa', 'bbb')