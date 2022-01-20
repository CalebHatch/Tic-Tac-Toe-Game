# Tic Tac Toe Game

## Dev Log

1/10/22 - Started writing program. Made print blocks for the board and a while loop to keep the game going while the "victory condition" is false. Oh, I added the existence of the "Victory" boolean as well. The bones were laid out for it to serve its function as the victory condition, but it currently is merely a prototype.

1/11/22 - Instead of the print block printing the same string again and again, I created a new string for each line. The while loop now prints the strings one line at a time. I also added an if block for x that utilizes the replace function to change the contents in the position of said strings. This way, the string can be manipulated by the user through said if block that determines which number the user entered and changes the number to an "X" or "O" accordingly. Allowing for the user manipulation makes it possible for the user to change the numbers to "X's" or "O's". Added "x1, x2, x3, ..." boolean variables in order for victory definitions to be easily written later. Only started adding the intial if block and first few "x1, x2, x3, ..." boolean variables. Today, I just wanted to make sure the idea in my head would work, and it does.

1/11 contd. - Finished writing for all the cases in which the user inputs a value. I also set a bunch of conditions for if the user tries to occupy a space that's used by either another user or themselves, and I set a condition for if a user inputs a value other than 1-9. Wrote all the different victory conditions with custom messages based on who won.

Dev To-Do's (ARCHIVED):
(DONE on 1/11/22)1. make the print block into arrays so the user can change
them and to configure win conditions // didn't need to put in arrays thanks
to .replace.
(Written on 1/10/22)

(DONE on 1/11/21) 2. possibly use nested if block for victory conditions.
2a. maybe a nested if block could be used by making it for every combo
of moves either x or o would need to win.
2b. maybe only two if blocks would be needed. one for x and one for o.
(Written on 1/10/22)
2c. use the x1, x2, x3, etc boolean values in order to easily set win
conditions
(Written on 1/11/22)
