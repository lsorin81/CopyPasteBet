from django.db import models


class bookmaker(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to="CPBet/static")


class bet(models.Model):
# event based
    event_description = models.CharField(max_length=100)
# 'date published' = It is just verbose_name - something like human description or label for field.
    event_date = models.DateTimeField('event played date')
    event_result = models.CharField(max_length=25)
# bet based
    bet_description = models.CharField(max_length=100)
    bet_code = models.CharField(max_length=25)
    bet_bookmaker = models.ForeignKey(bookmaker)
    bet_odds = models.FloatField()
    bet_amount = models.FloatField()
    bet_date = models.DateTimeField('bet accepted date')
    bet_type = models.CharField(max_length=12)
    bet_result = models.FloatField()

    class Meta:
        unique_together = ('bet_date', 'bet_odds')

    def __unicode__(self):
        return self.event_description


class english_premier_league_result(models.Model):
    date = models.DateTimeField()
    home_team = models.CharField(max_length=25)
    away_team = models.CharField(max_length=25)
    result = models.CharField(max_length=3)


class unique_token_key(models.Model):
    key_id = models.IntegerField(primary_key=True)
    key = models.CharField(max_length=5)








