from random import randrange

#data structures
board = {'a': {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}, 'b': {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}, 'c': {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}, #board
         'd': {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}, 'e': {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}, 'f': {1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}}
users_moves = [] #list to log all of the users existing moves
choices = [1,2,3,4,5,6,7,8,9] #possible number choices

def main(): #main compilier
    print("Hello, what is the color I am playing for?") #hello message
    user = input() #gets users input
    while True: #goes until question == no
        print("Please populate board with all existing moves (including your own)") #prompts the user to input moves 
        [x,y,color] = input().split(" ") #accepts user input
        populate_board(x,y,color) #populates the board 
        question = input("Keep Going?\n") #asks the user if they want to keep going 
        if question == 'no': #if no exit the loop 
            break
    on_board(user) #calls the make move function

def populate_board(x,y,color): #function is designed to populate the board data structure with user input
    for letter,numbers in board.items(): #traverses the row,columns pairs in the board structure
        for number in numbers.keys(): #checks the number values in the columns sections
            if letter == x and int(y) == number: #if the values match 
                numbers[number].append(color) #populate the 'cell' with the corrosponding color
                print("Game board: ")
                print(board) #print the edited board
                break #exit the loop
            else:
                pass #pass the remaining
    
def on_board(user): #function is designed to determine if the user has any existing moves on the board
    for letter,numbers in board.items(): #searches through the letters,numbers pairs in the board.items()
        for row,cell in numbers.items(): #searches through the row,cell pairs in the numbers.items()
            if user in cell: #checks if the user has populated the cell
                users_moves.append((letter, row)) #if yes add the move to the log
            else:
                pass #otherwise move on
    if users_moves == []: #if the list is empty 
        print(False) #return false
    else:
        print(True) #else return True

def make_move(user):
    if on_board(user) == True:
        pass
    else:
        for letter,numbers in board.items():
                for row,cell in numbers.items():
                    if cell == []:
                        x = randrange(0,4)
                        y = choices.pop(x)
                        break
        
def three_in_row(user):
    pass


main()
