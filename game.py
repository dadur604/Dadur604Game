from random import sample, uniform, choice, choices, randint, random

def cls():
    import subprocess as sp
    sp.call('cls',shell=True)

def mapGen():

    #Map Generation
    global avaliableTiles                           #How many avaliable tiles
    avaliableTiles = sample(range(1, 10), randint(5, 8))

    #Choses tile to spawn on
    global playerTile
    playerTile = choice(avaliableTiles)

    #Set Type of Tile (At least one friendly and hostile)
    global tileType
    tileType = {}
    n = 1
    for i in avaliableTiles:
        tileType[i] = choice(['friendly', 'hostile'])
    tileType[choice(avaliableTiles)] = 'hostile'
    tileType[playerTile] = 'friendly'
    #print(tileType)

    #Setting actions allowed at each tile
    global canBuy
    global canSleep
    global enemyLevel
    canBuy = {}
    canSleep = {}
    enemyLevel = {}
    for i in avaliableTiles:
        if tileType[i] == 'friendly':
            canBuy[i] = choice([True, False])
            canSleep[i] = choice([True, False])
        elif tileType[i] == 'hostile':
            enemyLevel[i] = randint(0, 5)

def updateMap():
    global tileDict
    global playerTile
    global tileMap
    global avaliableTiles

    #Creates tile map
    tileDict = {}
    for i in range(1, 10):
        tileDict[i] = '[x]'
    for i in avaliableTiles:
        tileDict[i] = '[%s]'%(i)
    tileDict[playerTile] = '[' + u'\u263A' + ']'
    #print(tileDict)
    global tileMap
    tileMap = '''
    {}{}{}
    {}{}{}
    {}{}{}
    '''.format(
    tileDict[7], tileDict[8], tileDict[9], tileDict[4],
    tileDict[5], tileDict[6], tileDict[1], tileDict[2], tileDict[3])

def start():
    mapGen()
    updateMap()
    global health
    global playerWeapon
    health = 100
    playerWeapon = ('fists', 0)
    print('What is your username?')
    username = input('>')
    print('Welcome, %s' %(username))
    print('''
        {0} This represents you.
        {1} This represents a tile you can visit. Press the number inside to visit this tile.
        {2} This represents a blocked tile.'''.format('[' + u'\u263A' + ']','[1]','[x]'))
    interact()

def moveTo():
    global tileMap
    global playerTile
    global avaliableTiles
    print(tileMap)
    print('Enter a number to move to that tile, or 0 to go back')
    next_move = input('>')
    cls()
    #Check to make sure input is a number
    try:
        next_move = int(next_move)
    except ValueError:
        print('Please enter a number!')
        moveTo()
    if next_move == 0:
        cls()
        interact()
    elif next_move > 9 or next_move < 0:
        print('The number must be between 0 and 9')
        moveTo()
    elif next_move == playerTile:
        print('You are already at %s'%(next_move))
        moveTo()
    elif int(next_move) in avaliableTiles:
        playerTile = int(next_move)
        print('You have moved to %s'%(next_move))
        print()
        interact()
    else:
        print('That tile is blocked')
        moveTo()

def interact():
    global playerTile
    global tileType
    global tileMap
    global enemyLevel
    global playerWeapon
    global win_chance
    curType = tileType[playerTile]
    updateMap()
    print(tileMap)
    print('You are on tile %s, which is a %s tile.'%(playerTile, curType))
    do_list = []
    if curType == 'friendly': #Create prompt of avaliable actions
        if canBuy[playerTile] == True:
            do_list.append('(B) Buy Items   ')
        if canSleep[playerTile] -- True:
            do_list.append('(S) Sleep (Restore Health)  ')
        do_list.append('(R) Raid city   ')
        do_list.append('(M) Move to another tile')

    if curType == 'friendly':
        print(''.join(do_list))
        next_action = input('>')
        cls()
        next_action = next_action.lower()
        if next_action == 'b':
            if canBuy[playerTile]:
                buy()
            elif not canBuy[playerTile]:
                print('You cannot buy at this tile!')
                interact() #Buy
        elif next_action == 's':
            if canSleep[playerTile]:
                sleep()
            elif not canSleep[playerTile]:
                print('You cannot sleep here!')
                interact() #Sleep
        elif next_action == 'r':
            print('Raiding a friendly territory will make it hostile, and yeild a random amount of money and loot. Chance of success depends on weapon.')
            print('Are you sure you want to raid this tile? Y or N')
            yes = input('>')
            yes = yes.lower()
            if yes == 'y':
                raid()
            elif yes == 'n':
                interact()
            else:
                print('Invalid input')
                interact() #Raid
        elif next_action == 'm':
            moveTo() #Move
        else:
            print('Invalid input.')
            interact()
    elif curType == 'hostile':
        print('(A) Attack   (S) Steal   (M) Escape')
        next_action = input('>')
        cls()
        next_action = next_action.lower()
        if next_action == 'a':
            dif = playerWeapon[1] - enemyLevel[playerTile]
            if dif == 0:
                win_chance = .5
            elif dif > 0 and dif < 2:
                win_chance = uniform(.5, .9)
            elif dif >= 2:
                win_chance = uniform(.9, 1)
            elif dif < 0 and dif > -2:
                win_chance = uniform(.2, .5)
            elif dif <= -2:
                win_chance = uniform(0, .2)
            win_chance = round(win_chance, 2)
            print('This tile\'s enemy level is %s. Your weapon, %s, has a level of %s.'%(enemyLevel[playerTile], playerWeapon[0], playerWeapon[1]))
            print('Your chance of success is %s. Do you want to attack? Y or N'%(win_chance))
            yes = input('>')
            yes = yes.lower()
            if yes == 'y':
                attack()
            elif yes == 'n':
                interact()
            else:
                print('Invalid input')

        elif next_action == 's':
            pass
        elif next_action == 'm':
            pass
        else:
            print('Invalid input.')
            interact()

def dead():
    print('You have died. Do you want to play again?')
    playAgain = input('Y or N \n')
    if playAgain == 'y':
        start()
    elif playAgain == 'Y':
        start()
    else:
        quit()

def checkDead():
    if health <= 0:
        dead()

def raid():
    print('Raiding...')
    interact()

def buy():
    print('Buying...')
    interact()

def sleep():
    print('Sleeping...')
    interact()

def attack():
    global win_chance
    win = choices((True, False), weights = [win_chance, (1 - win_chance)])
    print(win)

start()
