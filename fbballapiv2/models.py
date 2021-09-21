from django.db import models

# Create your models here.


class Player(models.Model):
    Player_Name = models.CharField(max_length=50)
    Team_Name = models.CharField(max_length=3)
    GP = models.IntegerField()
    MIN = models.FloatField()
    FGM = models.FloatField()
    FGA = models.FloatField()
    FG_PCT = models.FloatField()
    FG3M = models.FloatField()
    FTM = models.FloatField()
    FTA = models.FloatField()
    FT_PCT = models.FloatField()
    REB = models.FloatField()
    AST = models.FloatField()
    STL = models.FloatField()
    BLK = models.FloatField()
    TOV = models.FloatField()
    PTS = models.FloatField()
    Pos = models.CharField(max_length=20,default="")