import pandas as pd
import csv
import Scoreboard
# Initializing variables:
board = [ ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"] ]
current_player = True
theWinner = 0
# This function is display the game board:
def displayBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            print(board[i][j], end='')
            if j < 2:
                print(" | ", end='')
        print()
        if i < 2:
            print("-------------")
# This function check the result of the moves:
def checkResult(currentplayer):
    if currentplayer == False:
        verif = "X"
    elif currentplayer == True:
        verif = "O"
    y = 0
    w = 2
    winXO = 0
    for z in range(0,3):
        if board[0][y] == verif and board[1][1] == verif and board[2][w] == verif:
            if verif == "X":
                winXO = 1
            if verif == "O":
                winXO = 2
        y = 2
        w = 0
        if board[z][0] == verif  and board[z][1] == verif and board[z][2] == verif:
            if verif == "X":
                winXO = 1
            if verif == "O":
                winXO = 2
        if board[0][z] == verif  and board[1][z] == verif and board[2][z] == verif:
            if verif == "X":
                winXO = 1
            if verif == "O":
                winXO = 2
    return winXO
# This function processes the moves:
def round(currentplayer):
    if currentplayer == False:
        mark = "O"
        c = str(input("O player's turn:")).upper()
        while True:
            if (c != "A1" and c != "A2" and c != "A3" and c != "B1" and c != "B2" and c != "B3" and c != "C1" and c != "C2" and c != "C3"):
                c = str(input("O player's turn(Enter a valid value):")).upper()
            elif sum(x.count(c) for x in board) == 0:
                c = str(input("O player's turn(Enter a valid value):")).upper()
            else:
                break
    elif currentplayer == True:
        mark = "X"
        c = str(input("X player's turn:")).upper()
        while True:
            if (c != "A1" and c != "A2" and c != "A3" and c != "B1" and c != "B2" and c != "B3" and c != "C1" and c != "C2" and c != "C3"):
                c = str(input("X player's turn(Enter a valid value):")).upper()
            elif sum(x.count(c) for x in board) == 0:
                c = str(input("X player's turn(Enter a valid value):")).upper()
            else:
                break
    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == c:
                board[i][j] = mark
    currentplayer = not currentplayer
    return currentplayer
# Running the game:
pX = input("Player name X:")
Scoreboard.newPlayer(pX.upper())
pO = input("Player name O:")
Scoreboard.newPlayer(pO.upper())
displayBoard()
for p in range(0,9):
    if theWinner == 0:
        current_player = round(current_player)
        theWinner = checkResult(current_player)
    if theWinner == 1:
        displayBoard()
        print("The player X won!!")
        fdf = Scoreboard.addWins(pX).sort_values(by=["wins"], ascending = False)
        fdf.reset_index(drop=True, inplace=True)
        fdf.index += 1
        print(fdf)
        break
    if theWinner == 2:
        displayBoard()
        print("The player O won!!")
        fdf = Scoreboard.addWins(pO).sort_values(by=["wins"], ascending = False)
        fdf.reset_index(drop=True, inplace=True)
        fdf.index += 1
        print(fdf)
        break
    if theWinner == 0 and p == 8:
        print("Draw!!")
    displayBoard()