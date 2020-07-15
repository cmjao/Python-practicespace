guess = int(input('Please guess a number between 1 to 10'))
secret = 4

if guess < secret:
    print('Too low')
elif guess > secret:
    print('Too high')
else:
    print('Just right!!!')