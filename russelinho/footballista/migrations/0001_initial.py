# Generated by Django 3.1.7 on 2021-03-31 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FootballPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_lastname', models.CharField(max_length=200)),
                ('player_dribbling_skill', models.DecimalField(decimal_places=0, max_digits=3)),
                ('player_passing_skill', models.DecimalField(decimal_places=0, max_digits=3)),
                ('player_shooting_skill', models.DecimalField(decimal_places=0, max_digits=3)),
                ('player_defending_skill', models.DecimalField(decimal_places=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='TeamName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_team_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_in_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='footballista.footballplayer')),
            ],
        ),
    ]
