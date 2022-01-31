#Varun Mukund
#1/27/22
#Rock Paper Scissors Game


#PSEUDOCODE
#   Menu
#   Assign a number to rock, paper, and scissors
#   Ask User to pick rock, paper, or scissors - translate that into the number assigned
#   Tell computer to pick random number, then translate that into rock paper or scissors
#   if statemetns for who wins
#   print statements for who wins etc


import os, random, time

os.system ('cls')

def menu():
    print ('{---------------------------------------------------------}')
    print ('{                                                         }')
    print ('{                                                         }')
    print ('{                                                         }')
    print ('{I bet I can beat in you in a game of ROCK PAPER SCISSORS!}')
    print ('{                   For Rock - Type 1                     }')
    print ('{                   For Paper - Type 2                    }')
    print ('{                   For Scissors - Type 3                 }')
    print ('{                                                         }')
    print ('{                                                         }')
    print ('{                                                         }')
    print ('{---------------------------------------------------------}')
    print ('What is your move? Look above to see how to pick an object')




# print ('--------')
# print (Choice)
# print (myNumber)
score = 0
myScore = 0
GameOn = True
print ('The score is', score, '-', myScore)
while (GameOn):
    menu()
    Menu = True
    while (Menu):
        try: 
            Choice = int(input(' '))
            if Choice>0 and Choice<4:
                Menu = False
            else:
                print ('That wasn\'t what I asked. Please enter a correct value')
        except ValueError:
            print ('That wasn\'t what I asked. Please enter a correct value')            
    myNumber = random.randint (1,3)
    if Choice == 1:
        print (' ')
        print (' ')
        print ('You picked 💎ROCK💎')
        if myNumber == 1:
            print('I picked 💎ROCK💎 as well!\n --- 👍We TIED👍---')
            print (' ')
            print ('The score is', score, '-', myScore)
        elif myNumber == 2:
            print (' ')
            print ('I picked 📃PAPER📃\n --- ✨I WIN!✨---')
            myScore = myScore + 1
            print (' ')
            print ('The score is', score, '-', myScore)
        else:
            print (' ')
            print ('I picked ✂ SCISSORS ✂... You win...')
            score = score + 1
            print (' ')
            print ('The score is', score, '-', myScore)
    elif Choice == 2:
        print (' ')
        print (' ')
        print ('You picked 📃PAPER📃')
        if myNumber == 1:
            print (' ')
            print('I picked 💎ROCK💎!\n --- DARN! You win, I will get you next time though!---')
            score = score + 1
            print (' ')
            print ('The score is', score, '-', myScore)
        elif myNumber == 2:
            print (' ')
            print ('I picked 📃PAPER📃 AS WELL\n --- 👍We TIED👍---')
            print (' ')
            print ('The score is', score, '-', myScore)
        else:
            print (' ')
            print ('I picked ✂ SCISSORS ✂... ✨I WIN!✨...')
            myScore = myScore + 1
            print (' ')
            print ('The score is', score, '-', myScore)
    elif Choice == 3:
        print (' ')
        print ('You picked ✂ SCISSORS ✂')
        if myNumber == 1:
            print (' ')
            print('I picked 💎ROCK💎!\n ---✨I WIN!✨---')
            myScore = myScore + 1
            print (' ')
            print ('The score is', score, '-', myScore)
        elif myNumber == 2:
            print (' ')
            print ('I picked 📃PAPER📃\n --- DARN! You win, I will get you next time though!---')
            score = score + 1
            print (' ')
            print ('The score is', score, '-', myScore)
        else:
            print (' ')
            print ('I picked ✂ SCISSORS ✂... 👍We TIED👍...')
            print (' ')
            print ('The score is', score, '-', myScore)

    Replay =  input('Would you like to play another round? Type "y" for yes or "n" for no\n')
    if Replay.lower() == str('n') or Replay.lower() == str('no'):
        os.system ('cls') 
        print (' ')
        print (' ')
        print ('The end score of our match was', score, '(you) -', myScore, '(me)')
        if myScore > score:
                print ('🏆🏆I WON THE GAME🏆🏆 - good try rookie.🤣🤣')
        elif score > myScore:
            print ('😭😭I lost...😭😭 It must have been rigged. 👺👺I will get my revenge!👺👺')
        elif score == myScore:
            print ('Well, we tied. 🤠🤠You are a worthy opponent🤠🤠')
            print (' ')
        print ('Nevertheless, Come back soon! 🎉🎉')
        print (' ')
        print (' ')
        GameOn = False
    elif Replay.lower () == str('y') or Replay.lower() == str('yes'):
        os.system('cls')
        print ('Preparing another round - for your own demise 😈')
        time.sleep(2)
        os.system('cls')
        menu()   
    else:
        os.system('cls')
        print ('That did not answer my question. I am kicking you out because you are mean!!')
        print (' ')
        GameOn = False
        
        
    




