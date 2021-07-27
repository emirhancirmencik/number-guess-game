from random import random
import os


# DEFAULT LIST OF PLAYERS AND INFORMATIONS FOR THE GAME
players = [ 
    { "id": 0, "name": "Player1", "score": 0, "exit": False },
    { "id": 1, "name": "Player2", "score": 0, "exit": False }
]

# DEFAULT LIST OF COUNTS AND INFORMATIONS FOR EACH ROUND
counts = [
    { "id": 0, "move": 0 },
    { "id": 1, "move": 0 }
]
    

# A FUNCTION THAT CLEARS CONSOLE
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
# A FUNCTION THAT PRINTS SCORES
def score():
    for i in range(0,len(players)):
        print('{0}\'s score:{1}'.format(players[i]["name"],players[i]["score"]))


# A FUNCTION THAT ADDS MORE PLAYER
def more_player(number):
    for i in range(3,number+1):
        player = { "id": i-1, "name": f"Player{i}", "score": 0, "exit": False}
        players.append(player)
        count = { "id": i-1, "move": 0 }
        counts.append(count)


# A FUNCTION THAT CHANGES CURRENT PLAYER
def change_player(current_player): 
    if current_player + 1 == len(players):
        current_player = 0
        return current_player
    else:
        return current_player + 1


# A FUNCTION THAT ASKS WHETHER PLAYER WANTS TO EXIT OR CONTINUE
def ask_exit(current_player):
    while(1):
        check = input("Do you want to exit? (Y/n):")
        if check.isdigit() == True:
            check = input("Yes or No ?: ")
        if check.lower() in ("y", "yes"):
            players[current_player]["exit"] = True
            break
        elif check.lower() in ("n", "no"):
            break
        
        
# A FUNCTION THAT CHECKS DOES ANY PLAYER WANT TO EXIT OR CONTINUE
def check_exit():
    counter = 0
    for player in players:
        if player["exit"] == True:
            counter += 1
    if counter >=1:
        return True
    else:
        return False
        
        
# A FUNCTION THAT ASKS HOW MANY PLAYER WANTS TO PLAY
def player_quantity():
    number = 0
    while(1):
        number = input("How many players want to play? (DEFAULT 2): ")
        if number.isdigit() == 1 or number == "":
            break
        else:
            pass      
    if number == "":
        number = 2
        
    return int(number) 


# A FUNCTION THAT ALLOWS PLAYER TO CHANGE HIS/HER NAME
def change_name(current_player):
    name = input(f"Player{current_player + 1} what is your name (DEFAULT Player{current_player + 1}): ")
    if name != "":
        players[current_player]["name"] = str(name)


# A FUNCTION THAT ALLOWS PLAYER TO MAKE GUESS
def guess(current_player):
    guess = 0
    while(1):
        guess = input(f'It\'s {players[current_player]["name"]}\'s turn make your guess: ')
        if guess.isdigit() == 0:
            print("You must enter a valid expression.")
        else:
            if int(guess) > 100 or int(guess) < 0:
               print("You must enter a number between 0 and 100.")
            else:
                break
    return int(guess)
       
     
# CHECKS THE GUESS IS WHETHER MORE BIGGER OR SMALLER THE RANDOM NUMBER ADD COUNTS HIS MOVES
def check(random, player_number, current_player):
    if player_number > random:
        counts[current_player]["move"] += 1
        print(f"""Your guess must be less than {player_number}. You have made {counts[current_player]["move"]} moves.""")
        return False
    elif player_number < random:
        counts[current_player]["move"] += 1
        print(f"""Your guess must be more than {player_number}. You have made {counts[current_player]["move"]} moves.""")
        return False
    else:
        counts[current_player]["move"] += 1
        print(f"""Congratulations you found the number after {counts[current_player]["move"]} moves.""")
        return True


# GIVES POINT TO THE PLAYERS  
def point(game_quantity, final):
    moves = [x["move"] for x in counts]
    winner = min(moves) # FINDS MIN MOVE
    if moves.count(winner) > 1: # IF THERE IS MORE THAN 1 PLAYER THAT HAS MINIMUM MOVE QUANTITIY THERE IS NO WINNER
        winner = -1
    else:
        winner = moves.index(winner) # INDEX OF MINIMUM MOVE EQUALS TO THE ID OF THE PLAYER (YOU CAN SEE ID FROM DICTIONARY LIST IN TOP OF PAGE)
        
    if winner != -1:
        if game_quantity <= 5:
            players[winner]["score"] += 5
        if game_quantity > 5:
            if final == False:
                players[winner]["score"] += 10
            if final == True:
                players[winner]["score"] += 15


# ASKS FINAL MATCH AND CHECKS WHETHER IS IT NECESSARY
def final_match(game_quantity):
    scores = [x["score"] for x in players]
    
    winner_score = max(scores)
    
    scores = [x for x in scores if x != winner_score]
    
    second_winner_score = max(scores)
    
    if winner_score - second_winner_score > 15:
        return False
    
    while(1):
        check = input("Do you want to play final match? (Y/n):")
        if check.isdigit() == True:
            check = input("Yes or No ?: ")
        if check.lower() in ("y", "yes"):
            return True
        elif check.lower() in ("n", "no"):
            return False
        
# RESET COUNTS

def res_counts():
    for i in range(len(counts)):
        counts[i]["move"] = 0        

# CALCULATES WINNER

def calc_winner():
    scores = [x["score"] for x in players]
    
    winner_score = max(scores)
    
    if scores.count(winner_score) > 1:
        print("There is no winner game is tie.")
    else :
        winner = scores.index(winner_score)
        print(f"{players[winner]['name']} wins. His score is {players[winner]['score']}.")
    
    
    

   
def main():
    print("\n"*3)
    print("Welcome to the number guess game. If you see (DEFAULT) values in questions, you can just press enter for default answer.")
    print("\n"*3)
    current_player = players[0]["id"]
    quantity = player_quantity() #GET HOW MANY PLAYER WANTS TO PLAY
    more_player(quantity) # ADD PLAYERS
    game_quantity = 0
    final = False
    for i in range(0, len(players)): # CHANGES NAMES 
        change_name(i)
    
    while(1): # WORKS UNTIL GAME IS DONE
        cls()
        score()
        print(f"{game_quantity} game has played.") #PRINTS HOW MUCH GAME HAS PLAYED
        number = int(random()*100+1)
        
        while(1): # WORKS UNTIL PLAYER'S GUESS AND RANDOM NUMBER ARE EQUALS
            player_guess = guess(current_player)
            game_stat = check(number, player_guess, current_player)
            if game_stat == True: # IF PLAYER FOUND THE NUMBER
                if final != True: # IF IT WAS NOT A FINAL MATCH
                    ask_exit(current_player) # ASKS TO PLAYER EXIT OR CONTINUE
                break
         
        if current_player == len(players)-1: # IF CURRENT PLAYER IS THE LAST PLAYER
            game_quantity += 1 # INCREASE THE GAME COUNT
            point(game_quantity, final) # CALCULATE POINT
            res_counts() # RESET PLAYER MOVES
            if final == True: # IF IT WAS FINAL MATCH BREAK WHILE (GAME IS DONE)
                break
            if check_exit() == True: # IF ANYBODY WANTS TO EXIT
                if game_quantity <= 5: # IF NUMBER OF GAMES LESS AND EQUAL THAN 5
                    cls()
                    break # GAME IS DONE
                else:
                    final = final_match(game_quantity) # CHECK THE FINAL MATCH IS AVAILABLE AND ANYBODY WANTS IT
                    if final != True: # IF NOBODY WANTS OR IT IS NOT AVAILABLE
                        break # GAME IS DONE
        current_player = change_player(current_player) # CHANGES THE CURRENT PLAYER
    
    cls()
    score() #PRINT SCORES  
    calc_winner() #PRINT WINNER
    
if __name__ == "__main__":
    main()
    











