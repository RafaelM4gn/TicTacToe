import pandas as pd 
import csv
#Esta funçao é responsável por adicionar um novo jogador
def resetDf():
    df = pd.read_csv("./Scoreboard.csv")
    df.index += 1
    return df
def newPlayer(player):
    with open('Scoreboard.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([player, '1'])
    resetDf()
    return resetDf()
#Esta funçao é responsável por aumentar as vitorias de um jogador
def addWins(name):
    df = resetDf()
    df.loc[df["name"]== name , "wins"] +=  1
    df.to_csv("Scoreboard.csv", index=False)
    return resetDf()
#Esta função é responsável por inicializar o DataFrame
a = addWins("alisson")
a = newPlayer("modoki")
print(a)
