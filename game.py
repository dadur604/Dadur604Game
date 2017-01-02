def cls():
    import subprocess as sp
    sp.call('cls',shell=True)

def mapGen():
    from random import sample, uniform, choice

    #Map Generation
    global avaliableTiles                           #How many avaliable tiles
    avaliableTiles = sample(range(1, 10), int(uniform(5, 8)))

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
    cls()
    health = 100
    print('What is your username?')
    userName = input('>')
    print('Welcome, %s' %(userName))
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
    if next_move == '0':
        cls()
        interact()
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
    curType = tileType[playerTile]
    updateMap()
    print(tileMap)
    print('You are on tile %s, which is a %s tile.'%(playerTile, curType))
    if curType == 'friendly':
        print('(X) do_x     (Y) do_y    (Z) do_z    (M) Move to another tile')
        next_action = input('>')
        cls()
        next_action = next_action.lower()
        if next_action == 'x':
            pass
        elif next_action == 'y':
            pass
        elif next_action == 'z':
            pass
        elif next_action == 'm':
            moveTo()
        else:
            print('Invalid input.')
            interact()
    elif curType == 'hostile':
        print('(X) do_x     (Y) do_y    (Z) do_z    (M) Move to another tile')
        next_action = input('>')
        cls()
        next_action = next_action.lower()
        if next_action == 'x':
            pass
        elif next_action == 'y':
            pass
        elif next_action == 'z':
            pass
        elif next_action == 'm':
            moveTo()
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

start()
