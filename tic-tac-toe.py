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



if __name__ == "__main__":
    main()