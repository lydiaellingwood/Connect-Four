#Connect Four

This is a simple two player Connect Four program.

<img width="406" alt="image" src="https://github.com/user-attachments/assets/04f710f6-087e-40af-a0fb-5193fd7fe034" />

## Game Instructions

Instructions:
- Use L & R arrow keys or A & D keys to move your chip left and right and select the collumn where you want to place
- Press space, the down arrow key, or the S key to place a disk in your selected collumn
- First player to connect four of their colored disks wins!

## How it was made
Tech used: Python with use of the Pycharm library

This program makes use of three classes
- player: Holds information about each of the two players and can be used to hold the names of specific players
- board: Holds most of the techical information for the game in a matrix of lists. Checks to see if and when and if a player has won.
- game: Creates graphics and takes in user input for the front end of the game.

Winning mechanism:
- When checking if the player has won, the game only checks the rows, collumns and diagonals that cross through the last piece placed. This was done at the reccomendation of Jack Ellingwood.
- Out of those rows and collumns, the game only checks the rows, collumns and digonals that do not leave the board.

For bug testing this piece it is reccomended that the "verbose" variable set to true

## What I Learned

- How to write a better README.md file
- How to use the pygame library
