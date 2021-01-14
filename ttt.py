#Start
#Creating a tic-tac-toe board
def tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")

#Scoreboard

def scoreboard(score_board):
    print("\t********************************")
    print("\t         | SCOREBOARD |      ")
    print("\t********************************")
 
    players = list(score_board.keys())
    print("\t   ", players[0], "\t    ", score_board[players[0]])
    print("\t   ", players[1], "\t    ", score_board[players[1]])
 
    print("\t******************************\n")
 
#checking winner

def check_winner(player_pos, now_player):
    #winning combination.
    solution = [[1,2,3],[4,5,6],[7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    #check if above solution has been met. 
    for x in solution:
        if all(y in player_pos[now_player] for y in x):
            return True #if any above combination is satisfied
    
    return False #if no any combination is satisfied

#checking draw

def draw(player_pos):
    if len(player_pos['X']) + len(player_pos['0']) == 9:
        return True
    return False

#game
def game(now_player):
    values = ['' for x in range(9)] #tic-tac-toe
    player_pos = {'X':[], '0':[]} #position of X and O
    
    #game_loop
    while True:
        tic_tac_toe(values)
        #Exeption block for move input
        try:
            print("Player ", now_player,"turn. Choose Box? : ",end="")
            move = int(input())
        except ValueError:
            print("Try Again, Invalid Input!!!!")
            continue
        #Sanity Check for move input
        if move<1 or move >9:
            print("Try Again, Invalid Input!!!!")
            continue
        
        #Check if the box is akready occupied
        if values[move-1]!='':
            print("Try again, Box already filled!!!!")
            continue
        
        #updating the game after input
        
        #updating the box
        values[move-1]=now_player

        #updating positions
        player_pos[now_player].append(move)
        
        #calling winner function
        if check_winner(player_pos, now_player):
            tic_tac_toe(values)
            print("Player ", now_player, "is the winner.")
            print("\n")
            return now_player
        
        #calling draw function
        if draw(player_pos):
            tic_tac_toe(values)
            print("DRAW")
            print("\n")
            return 'D'
        
        #switching moves of players
        if now_player == 'X':
            now_player = '0'
        else:
            now_player = 'X'


if __name__ == "__main__":
    print("\n")
    player1 = input ("Enter the name of Player 1 : ")    
    print("\n")
    player2 = input ("Enter the name of Player 2 : ")
    print("\n")         
    
    #storing the player who choose X and 0
    now_player = player1

    #storing the choice of player
    player_choice = {'X': "", '0':""}

    #storing the options
    options = ['X', '0']
    
    #storing the initial scoreboard
    score_board = {player1: 0, player2: 0}
    scoreboard(score_board)
    
    #looping game for multiple games
    #loop will run until player exit the game
    while True:
        #player choices.
        print("Trun to choose for", now_player)
        print("Enter 1 for X")
        print("Enter 2 for 0")
        print("Enter 3 to exit")
        
        try:
            choice = int(input())
        except ValueError:
            print("Try Again, Invalid Input!!!!")
            continue
        
        #conditions for player choices
        if choice == 1:
            player_choice['X'] = now_player
            if now_player == player1:
                player_choice['0'] = player2
            else:
                player_choice['0'] = player1
                
        elif choice == 2:
            player_choice['O'] = now_player
            if now_player == player1:
                player_choice['X'] = player2
            else:
                player_choice['X'] = player1
         
        elif choice == 3:
            print("Final Scores")
            scoreboard(score_board)
            break  
 
        else:
            print("Try Again, Invalid Choice\n")
        
        #storing the winner in a single game
        winner = game(options[choice-1])
        
        if winner != 'D':
            player_won = player_choice[winner]
            score_board[player_won] = score_board[player_won] + 1
        
        scoreboard(score_board)
        # Switch player who chooses X or O
        if now_player == player1:
            now_player = player2
        else:
            now_player = player1
               