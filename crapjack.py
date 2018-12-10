play = ''
print("Welcome to Zethon's crapjack!")

money = 5000

while play != 'No':
    print('You have $' + str(money) + '. Place your bets.')
    bet = input()
    if int(bet) <= money:
        print('You put in ' + str(bet) + '. Type "deal" to begin.')
    deal = input()
    if deal.lower() == 'deal':
        import random
        for x in range(1):
            house = (random.randint(1,11))
            player =  (random.randint(2,21))
            print('House:' + str(house))
            print('Player:' + str(player) + ' Would you like to hit?')

        theLoop = ''
        while theLoop != 'no':
            print('Would you like to hit?')
            hitMe = input()
            if hitMe.lower() == 'yes':
                player = player + (random.randint(1,11))
                print('House:' + str(house))
                print('Player:' + str(player))

                if player > 21:
                    print('Player busts, house wins.')
                    money = int(money) - int(bet)
                    break
            else:
                break

        else:
            house = house + (random.randint(1,11))
            print('House:' + str(house))
            print('Player:' + str(player))
            import time
            time.sleep(2)

        if house < 17 and 22 and player < 22:
            print('House begins to draw...')
            import time
            time.sleep(2)
            house = house + (random.randint(1,11))
        if house < 17 and 22 and player < 22:
            house = house + (random.randint(1,11))
        if house < 17 and 22 and player < 22:
            house = house + (random.randint(1,11))
        if house < 17 and 22 and player < 22:
            house = house + (random.randint(1,11))
        if house < 17 and 22 and player < 22:
            house = house + (random.randint(1,11))
    print('House: ' + str(house))
    print('Player: ' + str(player))

    if house > 21:
        print('House busts, Player wins WOOOHOOOO')
        money = int(money) + int(bet)
    elif house > player and house < 22:
        print('House wins! Better luck next time!')
        money = int(money) - int(bet)
    elif house == player and house < 22:
        print('Push!')
    elif house < player and house < 22 and player < 22:
        print ('Player wins!')
        money = int(money) + int(bet)

print('YOU NOW HAVE ' + str(money))
        
print('Thank you for rolling, would you like to try again?')
play = input()

print('Thanks for Rolling')
