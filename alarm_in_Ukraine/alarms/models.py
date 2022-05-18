from django.db import models


class States(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=200)


class Alarm(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    alert = models.BooleanField()
    state_id = models.ForeignKey(States, on_delete=models.CASCADE)
