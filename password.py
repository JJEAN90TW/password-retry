password = '123456'
t = 3 # chance left
while t > 0:
    pwd = input('please enter your password:')
    if pwd == password:
        print('Log in!!')
        break # end
    else:
        t = t - 1
        print('ERROR!!', t, 'time(s) left!!')