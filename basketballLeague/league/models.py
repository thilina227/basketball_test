from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def natural_key(self):
        return self.name


class Player(models.Model):
    playerId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    height = models.FloatField()
    averageScore = models.FloatField()
    # numberOfGames = models.FloatField()  # this can be retrieved by games model
    team = models.ForeignKey(Team, related_name='players', null=True, on_delete=models.SET_NULL)
    # TODO authentication with django user
    # user = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def natural_key(self):
        return self.playerId


class League(models.Model):
    leagueId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)

    def natural_key(self):
        return self.leagueId


class Round(models.Model):
    roundId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    league = models.ForeignKey(League, related_name='rounds', on_delete=models.CASCADE)

    def natural_key(self):
        return self.roundId


class Game(models.Model):
    gameId = models.AutoField(primary_key=True)
    round = models.ForeignKey(Round, related_name='games', on_delete=models.CASCADE)
    firstTeam = models.ForeignKey(Team, related_name="firstTeam", null=True, on_delete=models.SET_NULL)
    secondTeam = models.ForeignKey(Team, related_name="secondTeam", null=True, on_delete=models.SET_NULL)
    firstTeamScore = models.IntegerField()
    secondTeamScore = models.IntegerField()
    winningTeam = models.ForeignKey(Team, related_name="winningTeam",  null=True, on_delete=models.SET_NULL)

    def natural_key(self):
        return self.gameId

    
class PlayerScoreByGame(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField()
