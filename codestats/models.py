from django.db import models
from django.contrib.auth import models as authmodels


# Create your models here.
class User(models.Model):
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def signin(self, nickname, password, samePassword):
        if password != samePassword:
            return "Passwords don't match.\nTry again"
        self.__init__(nickname=nickname, password=password)


class CodeUnit(models.Model):
    place = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

