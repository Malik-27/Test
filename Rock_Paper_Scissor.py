import random

while True:
    
    user_action=input('Enter rock, paper or scissor: ')
    possible_action= ['Rock', 'Paper', 'Scissor']
    computer_action= random.choice(possible_action)
    print('\n You choose {user_action}, Computer chooses {computer_action}\n')
    
    if user_action==computer_action:
        print('Both are same. It is a tie.')
    
    elif user_action == 'Rock':
        if computer_action== 'Paper':
            print('Paper covers stone.')
        else:
            print('Rock smashes scissor.')
    
    elif user_action == 'Scissor':
        if computer_action == 'Rock':
            print('Rock smashes scissor.')
        else:
            print('Paper covers rock.')
    
    elif user_action == 'Paper':
        if computer_action == 'Scissor':
            print('Scissor cuts paper')
        else:
            print('Paper covers stone')
            
    play_again=input('Play Again: (Y/N)')

    if play_again != 'Y':
        break