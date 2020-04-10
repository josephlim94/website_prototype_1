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

class GeneralTable(models.Model):
    listing_foreign_key = models.ForeignKey(ListingData, on_delete=models.CASCADE)
    general_data = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class DateTable(models.Model):
    listing_foreign_key = models.ForeignKey(ListingData, on_delete=models.CASCADE)
    date_data = models.DateField()
    description = models.CharField(max_length=200)

class TimeTable(models.Model):
    listing_foreign_key = models.ForeignKey(ListingData, on_delete=models.CASCADE)
    time_data = models.TimeField()
    description = models.CharField(max_length=200)

class PriceTable(models.Model):
    listing_foreign_key = models.ForeignKey(ListingData, on_delete=models.CASCADE)
    price_data = models.FloatField(default=0)
    description = models.CharField(max_length=200)