#Varun Mukund
#2/16/22
import os
os.system('cls')
#Card War game
numberCards=[]
for i in range(2,11):
    numberCards.append(i)
numberCards.insert(0,'A')
suits=['♠', '❤', '♣', '♦']
royals=['J', 'Q', 'K']
#Make a combined list [2,3,4,5,6,7,8,9,10,11,12,J,Q,K, etc...]
#Make combinations for every card ex: 2c, 2h, 5s ...
resultDeck=[]
def Deck(cardnumber):
    global suits
    global numberCards
    global resultDeck
    for i in range (len(suits)):
        suits[i]=str(numberCards[cardnumber])+str(suits[i])
    resultDeck.extend(suits)
    suits=['♠', '❤', '♣', '♦']
for l in range(0,8):
    Deck(1)
    Deck (2)
    Deck (3)
    Deck (4)
    Deck (5)
    Deck (6)
    Deck (7)
    Deck (8)
    Deck (9)

print ('The Card Deck:\n\n'+str(resultDeck))