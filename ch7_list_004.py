start1 = ['fee', 'fie', 'foe']
# (first, second)
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call the judge'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', 'say we are done'),
]
start2 = "Someone better"

# Line1 start1 (首字大寫、後面加上驚嘆號與空格) + first (首字大寫、後面加上驚嘆號)
# Line2 start2 + 空格 + second + 句點

for t in rhymes:
    print('! '.join(start1).title() + '!', t[0].capitalize() + '!')
    print(start2, t[1] + '.')