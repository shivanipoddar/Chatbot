from django.db import models


class Booking(models.Model):
    tperson = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    contact = models.IntegerField(blank=True, null=True)
    restype = models.CharField(blank=True, null=True, max_length=20)
    name = models.CharField(blank=True, null=True, max_length=20)

class Question(models.Model):
    que = models.CharField(max_length=50)

    def __str__(self):
        return self.que


class Choice(models.Model):
    choice = models.CharField(max_length=50)

    def __str__(self):
        return self.choice


class Conv(models.Model):
    conv = models.TextField(blank=True, null=True)
    user = models.CharField(max_length=20)

    def __str__(self):
        return self.user
