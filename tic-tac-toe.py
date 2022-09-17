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

def space_check()

def player_choise()

def full_board_check()

def winner_check_x()

def winner_check_o()

def draw_check()

def play_again()

if __name__ == "__main__":
    main()