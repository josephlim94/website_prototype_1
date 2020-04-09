from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class ListingData(models.Model):
    item_of_interest = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    proposed_date = models.DateTimeField('proposed date')
    def __str__(self):
        return self.item_of_interest