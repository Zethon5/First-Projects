loop1 = ''
print("Welcome to Zethon's game of go fish!")
import time
time.sleep(2)
print('When it is your turn, type in the number you want.')
print("If the computer tries to take a card you don't have")
print('it will automatically draw.')
import time
time.sleep(2)
import random
computer = [str(random.randint(1,13)), str(random.randint(1,13)),str(random.randint(1,13)),
            str(random.randint(1,13)),str(random.randint(1,13)),str(random.randint(1,13)),
            str(random.randint(1,13))]

player = [ str(random.randint(1,13)),str(random.randint(1,13)),str(random.randint(1,13)),
           str(random.randint(1,13)),str(random.randint(1,13)),str(random.randint(1,13)),
           str(random.randint(1,13)),]
print('')
print('Your hand:', player)

print('')

while len(player) and len(computer) > 0:
    while loop1 != 'no':
        print('Your move')
        yourMove = input()

        if yourMove not in player:
            print('You do not have that card, please try again.')
        elif yourMove in computer:
            computer.remove(yourMove)
            player.remove(yourMove)
            print('Success')
            print('Player hand now:', player)
            break
        elif yourMove not in computer:
            print("They don't have that card.")
            print('Player must go fish!')
            player.append(str(random.randint(1,13)))
            print('Player hand now:', player)
            break

    print("Computer's Turn")
    itMove = random.choice(computer)
    if itMove in player:
        computer.remove(itMove)
        player.remove(itMove)
        print('The computer takes your:', itMove)
    else:
        print('The computer fails to pick the right card, and draws one.')
        computer.append(str(random.randint(1,13)))

if len(computer) > len(player):
    print('Computer wins!')

if len(cmoputer) < len(player):
    print('Player wins!')

print('Thank you for playing, program will shut down in 10 seconds')
import time
time.sleep(10)
