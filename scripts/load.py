import csv
import os
from fbballapiv2.models import Player

#name	POS	Team	Games	Min	FG%	FGM	FGA	FT%	FTM	FTA	3PM	PTS	TREB	AST	STL	BLK	TO

def run():
    __location__ = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
    file = open(os.path.join(__location__,'cleaned.csv'))
    data=csv.reader(file)

    #data = pd.read_csv(os.path.join(__location__,'fantasyprojections2021v2.csv'))

    Player.objects.all().delete()
    count=1
    for player in data:
        if count==1:
            count= count + 1
            pass
        else:  
            print(player[0])
            Player.objects.create(Player_Name=player[0],Team_Name=player[2],GP=player[3],MIN=player[4],FGM=player[6],FGA=player[7],FG_PCT=round(float(player[5]),3),FG3M=player[11],FTM=player[9],FTA=player[10],FT_PCT=round(float(player[8]),3),REB=player[13],AST=player[14],STL=player[15],BLK=player[16],TOV=player[17],PTS=player[12],Pos=player[1])