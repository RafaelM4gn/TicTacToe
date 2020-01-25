import pandas as pd 
import csv

uri = "https://raw.githubusercontent.com/alura-cursos/introducao-a-data-science/master/aula1.2/ratings.csv"
df = pd.read_csv("./Scoreboard.csv")

#([[5, 6], [7, 8]], columns=list('AB'))
def newPlayer(player):
    with open('Scoreboard.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        spamwriter.writerow(['1',player, '5'])
newPlayer("sla")
df.loc[df["name"]=="rafael", "wins"] = 500
df.to_csv("Scoreboard.csv", index=False)
print(df)
