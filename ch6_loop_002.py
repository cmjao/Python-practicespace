guess_me = 7
number = 1

while True:
    if number < guess_me:
        print('%d too low' % number)
        number += 1
    elif number == guess_me:
        print('%d found it!' % number)
        number += 1
        continue
    else:
        print('%d oops' % number)
        break
    

