from django.conf import settings
from django.db import models


class Test(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Quest(models.Model):
    question = models.CharField(max_length=200)
    tip=models.CharField(max_length=1)
    test = models.ForeignKey('Test',on_delete=models.CASCADE,)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=200)
    quest = models.ForeignKey('Quest',on_delete=models.CASCADE,)

    def __str__(self):
        return self.answer

class Schools(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    description = models.TextField()
    test = models.ForeignKey('Test',on_delete=models.CASCADE,)

    def __str__(self):
        return self.name
        return self.link
        return self.description