from django.db import models

unprocessedString = "19:30	Sunderland - Manchester United	1:2	7.00	4.53	1.65	29"


class bets(models.Model):
# event based
    event_description = models.CharField(max_length=100)
# 'date published' = It is just verbose_name - something like human description or label for field.
    event_date = models.DateTimeField('event played date')
    event_result = models.CharField(max_length=25)
# bet based
    bet_description = models.CharField(max_length=100)
    bet_code = models.CharField(max_length=25)
    bet_bookmaker = models.CharField(max_length=25)
    bet_odds = models.FloatField()
    bet_amount = models.FloatField()
    bet_date = models.DateTimeField('bet accepted date')
    bet_type = models.CharField(max_length=12)
    bet_result = models.FloatField()

    class Meta:
        unique_together = ('bet_date', 'bet_odds')

    def __unicode__(self):
        return self.event_description


class english_premier_league_results(models.Model):
    date = models.DateTimeField()
    home_team = models.CharField(max_length=25)
    away_team = models.CharField(max_length=25)
    result = models.CharField(max_length=3)