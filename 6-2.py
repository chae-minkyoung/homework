guess_me=7
number = 8
while number < guess_me:
    print('too low')
    break
else:
    while number == guess_me:
        print('found it')
        break
    else:
        print('too high')
