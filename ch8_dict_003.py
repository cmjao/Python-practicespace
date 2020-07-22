squares = {num : num ** 2 for num in range(10)}
print(squares)

odd = {num for num in range(10) if num % 2 == 1}
print(odd)

for num in range(10):
    print('Got', num)

tuple_1 = ('optimist', 'pessimist', 'troll')
tuple_2 = ('The glass is haif full', 'The glass is half empty', 'How did you get a glass?')
print(dict(zip(tuple_1, tuple_2)))

titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
print(dict(zip(titles, plots)))