from django.contrib import admin

from .models import FootballPlayer, Teams, TeamName

admin.site.register(FootballPlayer)
admin.site.register(TeamName)
admin.site.register(Teams)
