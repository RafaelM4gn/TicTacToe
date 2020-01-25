import pandas as pd 
import csv
#Esta funçao é responsável por adicionar um novo jogador
def newPlayer(player):
    with open('Scoreboard.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow([player, '5'])
#Esta funçao é responsável por aumentar as vitorias de um jogador
def addWins(name):
    df.loc[df["name"]== name , "wins"] +=  1
    df.to_csv("Scoreboard.csv", index=False)
#leitura do DataFrame
df = pd.read_csv("./Scoreboard.csv")
df.index += 1
#---

print(df)
