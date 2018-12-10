import time
print("Welcome to Robert's madlibs!")
time.sleep(2)
moreStories = ''
while moreStories !="no":
    print('Please type "1" or "2" or "3" to pick a story!')
    story = input()

    if story == '1':
        print('Enter the name of a person')
        person = input()
        print('Enter the name of a place')
        place = input()
        print('Enter an adjective')
        adj1 = input()
        print('Enter a plural noun')
        plurNoun1 = input()
        print('Enter an adjective')
        adj2 = input()
        print('Enter a plural noun')
        plurNoun2 = input()
        print('Enter a place')
        place1 = input()
        print('Enter an action verb')
        actVerb = input()
        print('Enter a plural noun')
        plurNoun3 = input()
        print('Enter a noun')
        noun = input()
        print('Enter an action verb')
        actVerb1 = input()
        print('Enter an action noun')
        actVerb2 = input()
        print('Enter an adjective')
        adj3 = input()

        import time
        time.sleep(1)
        print('Thank you, making your story now!')

        import time
        time.sleep(3)

        print('Last summer, my mom and dod took me and ' + str(person) + ' on a trip to ' + str(place) + '.')
        print('The weather there is very ' + str(adj1) + '!')
        print('Northern ' + str(place) + ' has many ' + str(plurNoun1) + ', and they make ' + str(adj2) + ' ' + str(plurNoun2) + ' there.')
        print('Many people also go to ' + str(place1) + ' to ' + str(actVerb) + ' or see the ' + str(plurNoun3) + ' and are very proud of their big ' + str(noun) + '.')
        print('They also like to ' + str(actVerb1) + ' in the sun and swim in the ' + str(actVerb2) + '!')
        print('It was a really ' + str(adj3) + ' trip!')
        print(' ')

    elif story == '2':
        print('Please enter an adjective')
        a1 =input()
        print('Please enter a first name')
        a2 =input()
        print('Please enter an adjective')
        a3 =input()
        print('Please enter a noun')
        a4 =input()
        print('Please enter a verb')
        a5 =input()
        print('Please enter an animal')
        a6 =input()
        print('Please enter a verb ending in "ing"')
        a7 =input()
        print('Please enter an adverb')
        a8 =input()
        print('Please enter an adjective')
        a9 =input()
        print('Please enter a first name')
        a10 =input()
        print('Please enter an adjective')
        a11 =input()
        print('Please enter a noun')
        a12 =input()
        print('Please enter a a verb ending in "ing"')
        a13 =input()
        print('Please enter a plural noun')
        a14 =input()
        print('Please enter a verb ending in "ing"')
        a15 =input()

        import time
        time.sleep(1)
        print('Thank you, making your story now!')

        import time
        time.sleep(3)

        print(' ')
        print(' ')
        print("They say my school is haunted; my " + str(a1) + ' friend ' + str(a2) + ' says she saw a '  + str(a3) + ' ' + str(a4) + ' floating at the end of the hall near the caferteria.')
        print('Some say if you ' + str(a5) + " down that hallway at night, you'll hear a " + str(a6) + ' ' + str(a7) + ' ' + str(a8) + '.')
        print('My friend ' + str(a9) + ' ' + str(a10) + ' saw a ' + str(a11) + ' ' + str(a12) + '' + str(a13) + ' under one of the tables once.')
        print('I hope I never see any ' + str(a14) + ' ' + str(a15) + '; eating lunch there is scary enough!')

        import time
        time.sleep(4)
        print(' ')


    elif story == '3':
        print('Please enter a noun')
        b1=input()
        print('Please enter a noun')
        b2=input()
        print('Please enter a noun')
        b3=input()
        print('Please enter a noun')
        b4=input()
        print('Please enter a noun')
        b5=input()
        print('Please enter a noun')
        b6=input()
        print('Please enter a verb')
        b7=input()
        print('Please enter a noun')
        b8=input()
        print('Please enter a noun')
        b9=input()
        print('Please enter a noun')
        b10=input()
        print('Please enter a verb')
        b11=input()
        print('Please enter a noun')
        b12=input()
        print('Please enter a noun')
        b13=input()
        print('Please enter an adjective')
        b14=input()
        print('Please enter an adjective')
        b15=input()
        print('Please enter a place')
        b16=input()

        import time
        time.sleep(1)
        print('Thank you, making your story now!')

        import time
        time.sleep(3)
        print(' ')
        print(str(b1) + ' and ' + str(b2) + ' wanted to go camping. First they needed a tent. They decided to make a tent out of ' + str(b3) + ' and ' + str(b4) + '.')
        print('Next they packed other things they would need for camping like ' + str(b5) + ' and ' + str(b6) +'.')
        print('They were ready to go! They started ' + str(b7) + ' into the wood. They got neverous when they saw a ' + str(b8) + '.')
        print('Then they realized it was just a silly ' + str(b9) + '. When they found a campsite they unpacked the ' + str(b10) + " and then decided to go " + str(b11) + '.')
        print('Now they were tired and asked their parents to help them make a campfire. They used ' + str(b12) + ' and ' + str(b13) + ' to build a fire.')
        print('It was very ' + str(b14) + '. They sat around the campfire telling ' + str(b15) + ' sotries.')
        print('Finally it was time to go to sleep. They had a great camping trip! Next time they want to camp at the ' + str(b16) + '!')

        import time
        time.sleep(4)
        print(' ')



    print('Would you like to play another?')
    moreStories = input()

print('Thank you for reading, good bye!')
import time
time.sleep(7)
