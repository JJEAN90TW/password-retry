password = '123456'
t = 3 # chance left
while t > 0:
    t = t - 1
    pwd = input('please enter your password:')
    if pwd == password:
        print('Log in!!GOOD JOB!!')
        break # end
    else:
        print('ERROR!!')
        if t > 0:
            print( t, 'time(s) left!!')
        if t == 0:
            print('WRONG LA!! GET OUT!!')