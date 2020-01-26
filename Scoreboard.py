import pandas as pd 
import csv
def resetDf():
    df = pd.read_csv("./Scoreboard.csv")
    df.index += 1
    return df
#Esta funçao é responsável por adicionar um novo jogador caso ele nao exista
def newPlayer(player):
    create = True
    with open('Scoreboard.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == player:
                create = False
                break
            else:
                create = True
        if create == True:
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
a = addWins("rafael")
print("---")
print(a)
