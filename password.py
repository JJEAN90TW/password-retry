password = '123456'
t = 3 # chance left
while True:
    pwd = input('please enter your password:')
    if pwd == password:
        print('Log in!!')
        break # end
    else:
        t = t - 1
        print('ERROR!!', t, 'time(s) left!!')
        if t == 0:
            print('WRONG LA!!')
            break