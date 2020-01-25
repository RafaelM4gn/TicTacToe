# Inicializando variáveis:
board = [ ["A1", "B1", "C1"], ["A2", "B2", "C2"], ["A3", "B3", "C3"] ]
current_player = True
theWinner = 0
# Esta função é responsável por exibir o tabuleiro do jogo:
def displayBoard():
    for i in range(0, 3):
        for j in range(0, 3):
            print(board[i][j], end='')
            if j < 2:
                print(" | ", end='')
        print()
        if i < 2:
            print("-------------")
# Esta função é responsável por verificar o resultado da jogada:
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
                # print("o jogador X venceu")
            if verif == "O":
                winXO = 2
                # print("o jogador O venceu")    
        y = 2
        w = 0       
        if board[z][0] == verif  and board[z][1] == verif and board[z][2] == verif:
            if verif == "X":
                winXO = 1
                # print("o jogador X venceu")
            if verif == "O":
                winXO = 2
                # print("o jogador O venceu") 
        if board[0][z] == verif  and board[1][z] == verif and board[2][z] == verif:
            if verif == "X":
                winXO = 1
                # print("o jogador X venceu")
            if verif == "O":
                winXO = 2
                # print("o jogador O venceu") 
    return winXO
# Esta função é responsável por processar as jogadas:
def round(currentplayer):
    
    if currentplayer == False:
        mark = "O"
        c = input("jogada de O:") 
        while True:
            if c != "A1" and c != "A2" and c != "A3" and c != "B1" and c != "B2" and c != "B3" and c != "C1" and c != "C2" and c != "C3":
                c = input("jogada de O(Digite um Valor válido):")
            else:
                break 
    elif currentplayer == True:
        mark = "X"   
        c = input("jogada de X:") 
        while True:
            if c != "A1" and c != "A2" and c != "A3" and c != "B1" and c != "B2" and c != "B3" and c != "C1" and c != "C2" and c != "C3":
                c = input("jogada de X(Digite um Valor válido):")
            else:
                break 
            
    for i in range(0, 3):
        for j in range(0, 3):
            #if board[i][j] != "X" or board[i][j] != "O":
            if board[i][j] == c:
                board[i][j] = mark
    currentplayer = not currentplayer
    return currentplayer
# Execução do jogo:
for p in range(0,9):
    displayBoard()
    theWinner = checkResult(current_player)  
    if theWinner == 0:
        current_player = round(current_player)
    elif theWinner == 1:
        print("O jogador X venceu!")
    elif theWinner == 2:
        print("O jogador O venceu!")
    if theWinner == 0 and p == 8:
        print("Deu velha!")
if current_player == False:
    print("Congratulations!!!")
    displayBoard()