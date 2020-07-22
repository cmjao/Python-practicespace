e2f = dict(dog = 'chuen', cat = 'chat', walrus = 'morse')

print(e2f)
print(e2f['walrus'])

f2e = {i[1] : i[0] for i in e2f.items()}

print(f2e)