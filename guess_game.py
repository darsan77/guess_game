secret_number = 5
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Please enter your guess number: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!!')
        break
    else:
        if guess_count != 3:
            print('Try again')
else:
    print('Sorry you have failed')