cats = ['Henri', 'Grumpy', 'Lucy']
animals = dict(cats = cats, octopi = '', emus = '')
life = dict(animals = animals, plants = '', other = '')

print(life.keys())
print(life['animals'])
print(life['animals']['cats'])