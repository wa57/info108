import random

def deal():
    #Dealer and player
    playerHand.append(drawCard())
    dealerHand.append(drawCard())
    try:
        print('Your hand:', playerHand[0], 'and a', playerHand[1], "\nThe dealer's hand:", dealerHand[0], 'and a hole card')
    except:
        pass

def drawCard():
    drawnCard = random.choice(deck)
    deck.remove(drawnCard)
    return drawnCard

def placeBet():
    bet = float(input('Place a bet between $5 and $50: '))
    while bet < 5 or bet > 50:
        bet = float(input('Place a bet between $5 and $50: '))

def newRound():
    global deck
    global dealerHand
    global playerHand
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10] * 4
    random.shuffle(deck)
    playerHand = []
    dealerHand = []
    #placeBet()
    for n in range(2):
        deal()

    input('')

newRound()
