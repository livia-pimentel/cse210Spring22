# Prove Assignment - Tic-Tac-Toe
# The objective of the game is to make a sequence of three identical symbols, whether in a 
# vertical, horizontal or diagonal line, while trying to prevent your opponent from doing
# the same. When one of the participants makes a like, he wins the game.

#  Author: Livia Macêdo Pimentel


grid = [1, 2, 3,4, 5, 6, 7, 8, 9]

def printGrid():
    """Show the board design"""
    print()
    print('',f'\033[36m{grid[0]}\033[0m', "|", f'\033[36m{grid[1]}\033[0m', "|", f'\033[36m{grid[2]}\033[0m')
    print("-+-+-+-+-")
    print('', f'\033[36m{grid[3]}\033[0m', "|", f'\033[36m{grid[4]}\033[0m', "|", f'\033[36m{grid[5]}\033[0m')
    print("-+-+-+-+-")
    print('', f'\033[36m{grid[6]}\033[0m', "|", f'\033[36m{grid[7]}\033[0m', "|", f'\033[36m{grid[8]}\033[0m')
    print()

    
def getNumber():
    """Taken the chosen number and make the necessary validations, if it's out of 1 to 9
    or letter is typed an error message appears and continues in th loop until a valid option is typed."""
    while True:
        try:
            number = int(input('choose your number: '))
            if number in range (1,10):
                return number
            else:
                print('\033[31mNot valid choice\033[0m')
        except ValueError:
            print('\033[31mThis is not a number. Try again!\033[0m')
            continue
    
    
def choose_player(player_):
    """Assigns the symbol 'X' or 'O' according to the player"""
    if player_ == 0:
        symbol = "X"
    else:
        symbol = "O"
    return symbol

def verify_winner(grid):
    """Check the changes of winning"""
     #Lines
    if (grid[0] == grid[1] and grid[0] == grid[2]):
        print(f'\033[33mPlayer {grid[0]} won!')
        return True
    elif (grid[3] == grid[4] and grid[3] == grid[5]):
        print(f'\033[33mPlayer {grid[3]} won!')
        return True
    elif (grid[6] == grid[7] and grid[6] == grid[8]):
        print(f'\033[33mPlayer {grid[6]} won!')
        return True

    #Columns
    elif (grid[0] == grid[3] and grid[0] == grid[6]):
        print(f'\033[33mPlayer {grid[0]} won!')
        return True
    elif (grid[1] == grid[4] and grid[1] == grid[7]):
        print(f'\033[33mPlayer {grid[1]} won!')
        return True
    elif  (grid[2] == grid[5] and grid[2] == grid[8]):
        print(f'\033[33mPlayer {grid[2]} won!')
        return True 

    #Diagonals
    elif  (grid[0] == grid[4] and grid[0] == grid[8]):
        print(f'\033[33mPlayer {grid[0]} won!')
        return True
    elif (grid[2] == grid[4] and grid[2] == grid[6]):
        print(f'\033[33mPlayer {grid[2]} won!')
        return True

    else:
        return False


def main(): 
    print('\033[32m\n=-=-=-= Tic-Tac-Toe =-=-=-=\033[0m')

    player = 0
    times = 0
    winner = False
    printGrid()

    while (winner == False):
        if player == 0:
            print('\033[34mPlayer X\033[0m', end=' ')
            choice = getNumber()
            
            if grid[choice-1] =='X' or grid[choice-1] =='O':
                print('\033[31mPosition already chosen. Try again!\033[0m')
                choice = getNumber()
            times += 1      
        elif player == 1:
            print('\033[35mPlayer O\033[0m', end=' ')
            choice = getNumber()           
            if grid[choice-1] =='X' or grid[choice-1] =='O':
                print('\033[31mPosition already chosen. Try again!\033[0m')
                choice = getNumber()
            times += 1    
        symbol = choose_player(player)
        grid[choice-1] = symbol
        printGrid()
        winner = verify_winner(grid)
        if winner == True:
            print()
            break
        if times == 9:
            print('\033[31mNo one won!\033[0m')
            print()
            break 
        if player == 0:
            player = 1
        elif player == 1:
            player = 0
        
if __name__ == "__main__":
    main()