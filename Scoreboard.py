import pandas as pd
import csv


#This function initializes the DataFrame
def resetDf():
    df = pd.read_csv("./Scoreboard.csv")
    df.index += 1
    return df
#This function adds a new player if it does not exist
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
                spamwriter.writerow([player, '0'])
    resetDf()
    return resetDf()
#This function increases a player's wins
def addWins(name):
    df = resetDf()
    df.loc[df["name"]== name , "wins"] +=  1
    df.to_csv("Scoreboard.csv", index=False)
    return resetDf()
