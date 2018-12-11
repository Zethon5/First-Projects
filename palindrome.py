def pc(theword):
    master = []
    master.append(theword)
    print(master)
    wordcheck = 'o' + theword
    if len(theword) % 2 == 0:
        for i in range(1, int((len(theword)/2))+1):
            if wordcheck[i].lower() == wordcheck[-(i)].lower():
                pass
            else:
                master.remove(theword)
                break


    if len(theword) % 2 != 0:
        for i in range(1, int(len(wordcheck)/2)):
            if wordcheck[i].lower() == wordcheck[-(i)].lower():
                pass
            else:
                master.remove(theword)
                break

    if len(master) == 0:
        print(theword, ' is not a palindrome.')

    if len(master) ==1:
        print(theword, 'is a palindrome')

while True:
    word = input('What word would you like to check? \n')
    if ' ' in word:
        print('No spaces please.')
    else:
        pc(word)
