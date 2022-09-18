from os import system, name
from time import sleep 

#Function to clear the screen
def clear ():
    if name == "nt":
        _ = system("cls")
    
def main():

    i = 1

    #Introducction to the game
    print("Welcome to Tic-Tac-Toe")
    print("")
    print("The first player will be 'X' and the second player will be 'O'")
    print("The order to play the game will be like this:")
    print("|1|2|3|\n|4|5|6|\n|7|8|9|")
    print("")
    sleep(5)
    print("Let's play")
    print("")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    print("")
    clear()
    print("|1|2|3|\n|4|5|6|\n|7|8|9|")

    display_board = ["#"] * 10
    
    while True: 
        
        game_starts = full_board_check(display_board)

        
        while not game_starts:

            position = player_choise(display_board)

            clear()

            if i % 2 == 0:
                marker = "O"
            else:
                marker = "X"

            place_marker(display_board, marker, int(position))

            board(display_board)
            
            i += 1

            if winner_check_x(display_board, marker):
                print("You won player 'X'")
                break
            elif winner_check_o(display_board, marker):
                print("You won player 'O'")
                break
            elif draw_check(display_board, marker):
                print("It is a draw")
                break

            game_starts = full_board_check(display_board)

        
        if not play_again():
            break
        else:
            clear()
            i = 1 

            print("First player will be 'X' and second player will be 'O'")

            display_board = ["#"] * 10

def board(display_board):

    default_board = """
|1|2|3|
|4|5|6|
|7|8|9|
"""
    for i in range(1, 10):
        if (display_board[i] == "X" or display_board[i] == "O"):
            default_board = default_board.replace(str(i), display_board[i])

        else:
            default_board = default_board.replace(str(i), " ")
        print(default_board)

def place_marker (display_board, marker, position):

    display_board[position] = marker

    return display_board

def space_check(display_board, position):

    return display_board[position] == "#"

def player_choise(display_board):

    choise = input("Please select an empty space between 1 to 9: ")

    while not space_check(display_board, int(choise)):
        choise = input("This space isn't free, please choose a free one: ")

    return choise

def full_board_check(display_board):

    return len([x for x in display_board if x == "#"]) == 1

def winner_check_x(display_board, mark):

    if display_board[1] == display_board[2] == display_board[3] == mark == "X":

        return True
    
    elif display_board[4] == display_board[5] == display_board[6] == mark == "X":
      
        return True
    
    elif display_board[7] == display_board[8] == display_board[9] == mark == "X":
        
        return True
    
    elif display_board[1] == display_board[4] == display_board[7] == mark == "X":
        
        return True
    
    elif display_board[2] == display_board[5] == display_board[8] == mark == "X":
        
        return True
    
    elif display_board[3] == display_board[6] == display_board[9] == mark == "X":
        
        return True
    
    elif display_board[1] == display_board[5] == display_board[9] == mark == "X":
        
        return True
    
    elif display_board[3] == display_board[5] == display_board[7] == mark == "X":
       
        return True

    else:
        return False

def winner_check_o(display_board, mark):

    if display_board[1] == display_board[2] == display_board[3] == mark == "O":
        return True
    
    elif display_board[4] == display_board[5] == display_board[6] == mark == "O":
      
        return True
    
    elif display_board[7] == display_board[8] == display_board[9] == mark == "O":
        
        return True
    
    elif display_board[1] == display_board[4] == display_board[7] == mark == "O":
        
        return True
    
    elif display_board[2] == display_board[5] == display_board[8] == mark == "O":
        
        return True
    
    elif display_board[3] == display_board[6] == display_board[9] == mark == "O":
        
        return True
    
    elif display_board[1] == display_board[5] == display_board[9] == mark == "O":
        
        return True
    
    elif display_board[3] == display_board[5] == display_board[7] == mark == "O":
       
        return True

    else:
        return False

def draw_check(display_board, mark):

    if display_board[1] == display_board[2] == display_board[3] == mark != "O":
        return True
    
    elif display_board[4] == display_board[5] == display_board[6] == mark != "O":
      
        return True
    
    elif display_board[7] == display_board[8] == display_board[9] == mark != "O":
        
        return True
    
    elif display_board[1] == display_board[4] == display_board[7] == mark != "O":
        
        return True
    
    elif display_board[2] == display_board[5] == display_board[8] == mark != "O":
        
        return True
    
    elif display_board[3] == display_board[6] == display_board[9] == mark != "O":
        
        return True
    
    elif display_board[1] == display_board[5] == display_board[9] == mark != "O":
        
        return True
    
    elif display_board[3] == display_board[5] == display_board[7] == mark != "O":

        return True

    elif display_board[1] == display_board[2] == display_board[3] == mark != "X":
        return True
    
    elif display_board[4] == display_board[5] == display_board[6] == mark != "X":
      
        return True
    
    elif display_board[7] == display_board[8] == display_board[9] == mark != "X":
        
        return True
    
    elif display_board[1] == display_board[4] == display_board[7] == mark != "X":
        
        return True
    
    elif display_board[2] == display_board[5] == display_board[8] == mark != "X":
        
        return True
    
    elif display_board[3] == display_board[6] == display_board[9] == mark != "X":
        
        return True
    
    elif display_board[1] == display_board[5] == display_board[9] == mark != "X":
        
        return True
    
    elif display_board[3] == display_board[5] == display_board[7] == mark != "X":
       
        return True

    else:
        return False

def play_again():

    again = input("Do you want to play again? (y/n): ") 

    if again.lower() == "y":

        return True

    elif again.lower() == "n":

        return False

if __name__ == "__main__":
    main()