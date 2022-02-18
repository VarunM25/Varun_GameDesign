#Varun Mukund
#2/16/22
import os
os.system('cls')
#Card Game
suits=['♠', '♦', '♣', '♥']
royals=['J', 'Q', 'K']
numberCards=[]
for i in range(2,11):
    numberCards.append(i) #putting numbers into the deck
numberCards.insert(0,'A') #adding ace to the deck
numberCards.extend(royals) #Adding royals now
#Make a combined list [2,3,4,5,6,7,8,9,10,11,12,J,Q,K, etc...]
#Make combinations for every card ex: 2c, 2h, 5s ...
resultDeck=[]
def Deck(cardnumber): #adds suits to the numbers - makes parameters for diff cards
    global suits
    global numberCards
    global resultDeck
    for i in range (len(suits)):
        suits[i]=str(numberCards[cardnumber])+str(suits[i])
    resultDeck.extend(suits)
    suits=['♠', '❤', '♣', '♦'] #resetting suites
for l in range(0,13):
    Deck(1)
print ('The Card Deck:\n\n'+str(resultDeck), '\n\n'+str(len(resultDeck)), 'cards\n')