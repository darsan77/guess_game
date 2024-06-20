while True:
    weight = int(input('Please enter your weight:'))
    unit = input('Enter K for kg(s) or L for Lb(s): ')
    if unit.lower() == 'k':
        converted = weight/0.45
        print(f'You are {converted} pounds')
        print("can't divide by zero")
     
    elif unit.upper() == 'L':
        converted = weight*0.45
        print('You are',converted, 'kilos')
    else:
        print('I had told (K) for kg or (L) for lbs')
    print('\n')