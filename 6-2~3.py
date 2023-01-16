guess_me = 7
number = 8
while number < guess_me:
    print('too low')
    number+=1
    break
else:
    while number == guess_me:
        print('found it')
        number+=1
        break
    else:
        print('oops')
        number+=1
