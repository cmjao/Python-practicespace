small_str = input('Is that samll ? (Y/N)')

if small_str == 'Y':
    small = True
elif small_str == 'N':
    small = False
else:
    print('You input a wrong value!')

print(small)

green_str = input('Is that green ? (Y/N)')

if green_str == 'Y':
    green = True
elif green_str == 'N':
    green = False
else:
    print('You input a wrong value!')

print(green)

if small:
    if green:
        print('This a pea!')
    else:
        print('This a cherry!')
else:
    if green:
        print('This a watermelon!')
    else:
        print('This a pumpkin!')