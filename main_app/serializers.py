from rest_framework import serializers
from .models import ListingData, ListingUserGroup, GeneralTable, DateTable, TimeTable, PriceTable

class ListingDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingData
        fields = ['id', 'item_of_interest', 'price', 'proposed_date']

class ListingUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingUserGroup
        fields = "__all__"

class GeneralTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralTable
        fields = ['id', 'listing_foreign_key', 'general_data', 'description']

class DateTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTable
        fields = ['id', 'listing_foreign_key', 'date_data', 'description']

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = ['id', 'listing_foreign_key', 'time_data', 'description']

class PriceTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceTable
        fields = ['id', 'listing_foreign_key', 'price_data', 'description']