'''
Tic-Tac-Toe
Written by: Caleb Hatch
'''
import os

x_turn = True
victory = False
x_win = False
o_win = False

# Sets all the spaces on the board as vacant intially
x1 = False
x2 = False
x3 = False
x4 = False
x5 = False
x6 = False
x7 = False
x8 = False
x9 = False

o1 = False
o2 = False
o3 = False
o4 = False
o5 = False
o6 = False
o7 = False
o8 = False
o9 = False

first_line = ("1|2|3")
second_line = ("-+-+-")
third_line = ("4|5|6")
fourth_line = ("-+-+-")
fifth_line = ("7|8|9")

def print_board():
    print("")
    print(first_line)
    print(second_line)
    print(third_line)
    print(fourth_line)
    print(fifth_line)
    print("")

# Will run the game only as long as neither user has won yet
def no_victory_loop():
    global first_line, second_line, third_line, fourth_line, fifth_line, x_turn, victory, x_win, o_win, x1, x2, x3, x4, x5, x6, x7, x8, x9, o1, o2, o3, o4, o5, o6, o7, o8, o9

    while victory == False:
        while x_turn == True:
            print_board()
            x_move = input("X's turn to choose a square (1-9): ")

            # Changes corresponding numbers on board to "X". sets x bool to true
            if x_move == '1':
                # Will only change number to "X" if a letter isn't occupying it
                if o1 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x1 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                first_line = first_line.replace('1', 'X')
                x1 = True
            elif x_move == '2':
                if o2 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x2 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                first_line = first_line.replace('2', 'X')
                x2 = True
            elif x_move == '3':
                if o3 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x3 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                first_line = first_line.replace('3', 'X')
                x3 = True
            elif x_move == '4':
                if o4 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x4 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                third_line = third_line.replace('4', 'X')
                x4 = True
            elif x_move == '5':
                if o5 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x5 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                third_line = third_line.replace('5', 'X')
                x5 = True
            elif x_move == '6':
                if o6 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x6 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                third_line = third_line.replace('6', 'X')
                x6 = True
            elif x_move == '7':
                if o7 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x7 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                fifth_line = fifth_line.replace('7', 'X')
                x7 = True
            elif x_move == '8':
                if o8 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x8 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                fifth_line = fifth_line.replace('8', 'X')
                x8 = True
            elif x_move == '9':
                if o9 == True:
                    print("O has already taken that space. Please select another.")
                    continue
                elif x9 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                fifth_line = fifth_line.replace('9', 'X')
                x9 = True
            # repeats the loop if 1-9 isn't inputted
            else:
                print("An error occurred. Please only print the numbers 1-9")
                continue

            x_turn = False

        # Checks for X victory condition
        if x1 == True & x2 == True & x3 == True:
            victory = True
            x_win = True
            continue
        elif x1 == True & x4 == True & x7 == True:
            victory = True
            x_win = True
            continue
        elif x7 == True & x8 == True & x9 == True:
            victory = True
            x_win = True
            continue
        elif x4 == True & x5 == True & x6 == True:
            victory = True
            x_win = True
            continue
        elif x2 == True & x5 == True & x8 == True:
            victory = True
            x_win = True
            continue
        elif x3 == True & x6 == True & x9 == True:
            victory = True
            x_win = True
            continue
        elif x1 == True & x5 == True & x9 == True:
            victory = True
            x_win = True
            continue
        elif x3 == True & x5 == True & x7 == True:
            victory = True
            x_win = True
            continue

        if x_turn == False:
            o_turn = True

        while o_turn == True:
            print_board()
            o_move = input("O's turn to choose a square (1-9): ")

            # Changes corresponding numbers on board to "O". sets o bool to true
            if o_move == '1':
                # Will only change number to "O" if a letter isn't occupying it
                if x1 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o1 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                first_line = first_line.replace('1', 'O')
                o1 = True
                o_turn = False
            elif o_move == '2':
                if x2 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o2 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                first_line = first_line.replace('2', 'O')
                o2 = True
                o_turn = False
            elif o_move == '3':
                if x3 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o3 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                first_line = first_line.replace('3', 'O')
                o3 = True
            elif o_move == '4':
                if x4 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o4 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                third_line = third_line.replace('4', 'O')
                o4 = True
            elif o_move == '5':
                if x5 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o5 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                third_line = third_line.replace('5', 'O')
                o5 = True
            elif o_move == '6':
                if x6 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o6 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                third_line = third_line.replace('6', 'O')
                o6 = True
            elif o_move == '7':
                if x7 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o7 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                fifth_line = fifth_line.replace('7', 'O')
                o7 = True
            elif o_move == '8':
                if x8 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o8 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                fifth_line = fifth_line.replace('8', 'O')
                o8 = True
            elif o_move == '9':
                if x9 == True:
                    print("X has already taken that space. Please select another.")
                    continue
                elif o9 == True:
                    print("You have already taken that space. Please select another.")
                    continue
                fifth_line = fifth_line.replace('9', 'O')
                o9 = True
            # repeats the loop if 1-9 isn't inputted
            else:
                print("An error occurred. Please only print the numbers 1-9")
                continue

            o_turn = False

        # Checks for O victory condition
        if o1 == True & o2 == True & o3 == True:
            victory = True
            o_win = True
            continue
        elif o1 == True & o4 == True & o7 == True:
            victory = True
            o_win = True
            continue
        elif o7 == True & o8 == True & o9 == True:
            victory = True
            o_win = True
            continue
        elif o4 == True & o5 == True & o6 == True:
            victory = True
            o_win = True
            continue
        elif o2 == True & o5 == True & o8 == True:
            victory = True
            o_win = True
            continue
        elif o3 == True & o6 == True & o9 == True:
            victory = True
            o_win = True
            continue
        elif o1 == True & o5 == True & o9 == True:
            victory = True
            o_win = True
            continue
        elif o3 == True & o5 == True & o7 == True:
            victory = True
            o_win = True
            continue

        if o_turn == False:
            x_turn = True

def main():
    global x_win, o_win, victory, first_line, second_line, third_line, fourth_line, fifth_line

    print("This is a game of Tic-Tac-Toe. Line up three of your letter to win!")

    no_victory_loop()
    print_board()

    # Displays custom message based on who won
    if x_win == True:
        print("X Wins!")
    elif o_win == True:
        print("O Wins!")

    # Ends the game once victory condition is met by a player
    if victory == True:
        print("Good game. Thanks for playing!")

    os.system('pause') # Screen won't auto disappear

if __name__ == '__main__':
    main()