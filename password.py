characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              '0','1','2','3','4','5','6','7','8','9','!','#','-','?','+']
print('Please enter the password:')
password = input()
tries = 0
for i in characters:
    crack = i
    tries = tries + 1
    if str(crack) == str(password):
        print('Password: ', str(crack), ' Tries: ', str(tries))
        quit()
print('Password Longer Than 1, after ', str(tries), ' tries.')

for i in characters:
    for x in characters:
        crack = i + x
        tries = tries + 1
        if str(crack) == str(password):
            print('Password: ', str(crack), ' Tries: ', str(tries))
            quit()
print('Password Longer Than 2, after ', str(tries), ' tries.')

for i in characters:
    for x in characters:
        for y in characters:
            crack = i + x + y
            tries = tries + 1
            if str(crack) == str(password):
                print('Password: ', str(crack), ' Tries: ', str(tries))
                quit()
print('Password Longer Than 3, after ', str(tries), ' tries.')

for i in characters:
    for x in characters:
        for y in characters:
            for z in characters:
                crack = i+x+y+z
                tries = tries + 1
                if str(crack) == str(password):
                    print('Password: ', str(crack), ' Tries: ', str(tries))
                    quit()
print('Password Longer Than 4, after ', str(tries), ' tries.')

for i in characters:
    for x in characters:
        for y in characters:
            for z in characters:
                for f in characters:
                    crack = i+x+y+z+f
                    tries = tries + 1
                    if str(crack) == str(password):
                        print('Password: ', str(crack), ' Tries: ', str(tries))
                        quit()
print('Password Longer Than 5, after ', str(tries), ' tries.')

for i in characters:
    for x in characters:
        for y in characters:
            for z in characters:
                for f in characters:
                    for l in characters:
                        crack = i+x+y+z+f+l
                        tries = tries + 1
                        if str(crack) == str(password):
                            print('Password: ', str(crack), ' Tries: ', str(tries))
                            quit()

print('Password Longer Than 6, after ', str(tries), ' tries.')
for i in characters:
    for x in characters:
        for y in characters:
            for z in characters:
                for f in characters:
                    for l in characters:
                        for r in characters:
                            crack = i+x+y+z+f+l+r
                            tries = tries + 1
                            if str(crack) == str(password):
                                print('Password: ',str(crack),' Tries: ', str(tries))
                                quit()
