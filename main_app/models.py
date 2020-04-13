from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class ListingData(models.Model):
    item_of_interest = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    proposed_date = models.DateTimeField('proposed date')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    current_users = models.ManyToManyField(User, through='ListingUserGroup')
    def __str__(self):
        return self.item_of_interest

class ListingUserGroup(models.Model):
    listing_id = models.ForeignKey(ListingData, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
    def __str__(self):
        return str(self.listing_id.item_of_interest) + ": " + str(self.user_id.username)

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