# Mastermind game
import random
import collections

print('Welcome to the Mastermind Game!')
print('Coded by Tan Jun San')

def menu():
    print()
    print('..MENU..')
    print('ENTER [1] Start!')
    print('      [2] Instructions (recomended for first time players)')
    print('You will have 12 attempts, Good luck!')
    print()
    selection = (input('Selection: '))
    return selection

def instructions():
    print()
    print('..Instructions..')
    print('[1] Guess the randomly generated 4 colour code with the right\n    colour and position!')
    print('[2] Select from [Red, Orange, Yellow, Green, Blue, Purple]')
    print('[3] Use the inital letters R,O,Y,G,B,P to represent the colours')
    print('[4] Type the code in a single line, eg. ROYG')
    print('[5] If you decide to quit at any point, type "end" ')
    print('[6] If you decide to reset the code, type "reset"')

# function for verifying the right position and colour (black peg)
def position():
    count = 0
    for x in range(4):
        if GuessList[x] == SecretList[x]:
            count = count + 1
    return count

# function to determine correct colour but wrong position
def colour():
    guesscounted = collections.Counter(GuessList)
    x1 = 0
    for k in counted:
        x = min(counted[k], guesscounted[k])
        x1 = x1 + x
    count2 = x1 - position()  # sets the right value of correct colour, wrong position
    return count2

# end game
def end():
    print('Sad to see you go :(. GOODBYE!')


# R, O, Y, G, B, P to represent red, orange, yellow, green, blue and purple.
list1 = ['R', 'O', 'Y', 'G', 'B', 'P']

#menu
while True:
    selection1 = menu()
    if selection1 == '1':
        break
    elif selection1 == '2':
        instructions()
        continue
    else:
        continue

# Mastermind game code 
game = True
while game:

    # randomly generate 4 colour code from colour list
    SecretList = []
    for x in range(4):
        SecretList.append(random.choice(list1))
    print(SecretList)
    print('Guess the code!')
    counted = collections.Counter(SecretList)

    z = 0
    # attempt loop
    while z < 12:
        z += 1
        count = 0
        # prompts user for colour guess and checks if it's valid
        while count != 4:
            count = 0
            GuessList = []
            non_colour = []
            Guess = (input('Guess: ')).upper()

            # to end game
            if Guess == ('end').upper():
                end()
                z = 13
                break
            # to reset game
            if Guess == ('reset').upper():
                z = 14
                break
                             
            # checks for only 4 input values
            if len(Guess) > 4:
                print('Only four colours. Try again')
            elif len(Guess) < 4:
                print('You are missing', 4 - len(Guess), 'colour(s)!')



            # check and display characters that is not in the colour list
            else:
                for i in range(4):
                    GuessList.append(Guess[i])  # append guess into list

                for x in range(4):

                    if GuessList[x] in list1:
                        count += 1
                        continue
                    elif GuessList[x] not in list1:
                        non_colour.append(GuessList[x])
                        continue
                if count < 4:
                    print(*non_colour, sep=", ", end=" ")
                    print('is not a colour')

        if z < 13:
            count1 = position()
            count2 = colour()
        elif z == 13:
            game = False
            continue
        elif z == 14:
            game = True
            continue
        # colour check
        if count1 < 4 and z < 12:
            print('Correct colour in the correct place: ', count1)
            print('Correct colour but in the wrong place: ', count2)
            print()
            continue

        # fail
        elif count1 < 4 and z == 12:
            print('You have failed all 12 attempts!. The answer was', SecretList)
            print('Better luck next time!')
            print()
        # win
        else:
            if z < 13:
                print('Congratulations! It took you', z, 'attempt(s)!')

        # repeat the game
        repeat = input('Do you want to play again? [Y/N]: ')
        if repeat.upper() == 'Y':
            break
        elif repeat.upper() == 'N':
            print('Thanks for playing!')
            game = False
            break
        else:
            while True:

                print('Y OR N???')
                repeat = input('Do you want to play again? [Y - Yes/ N - No]: ')
                if repeat.upper() == 'Y':
                    break
                if repeat.upper() == 'N':
                    print('Thanks for playing')
                    game = False
                    break
            break

# end of code
