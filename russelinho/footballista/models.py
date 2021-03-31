from django.db import models


class TeamName(models.Model):
    first_team_name = models.CharField(max_length=200)


class FootballPlayer(models.Model):
    player_lastname = models.CharField(max_length=200)
    player_dribbling_skill = models.DecimalField(max_digits=3, decimal_places=0)
    player_passing_skill = models.DecimalField(max_digits=3, decimal_places=0)
    player_shooting_skill = models.DecimalField(max_digits=3, decimal_places=0)
    player_defending_skill = models.DecimalField(max_digits=3, decimal_places=0)

    def __str__(self):
        return (
            f'Lastname: {self.player_lastname} '
        )


class Teams(models.Model):
    team_name = TeamName
    player_in_team = models.ForeignKey(FootballPlayer, on_delete=models.CASCADE)
