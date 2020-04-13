
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ListingData

def index(request):
    return render(request, 'main_app/index.html', {})

@login_required
def dashboard(request):
    listing_data_list = ListingData.objects.all()
    return render(request, 'main_app/dashboard.html', {'listing_data_list':listing_data_list})

def user_logout(request):
    logout(request)
    return redirect('main_app:index')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main_app:dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'main_app/signup.html', {'form': form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('main_app:dashboard'))
                else:
                    return HttpResponse("Your account was inactive.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details given")
        else:
            form = AuthenticationForm()
        return render(request, 'main_app/login.html', {'form': form})
    else:
        return redirect('main_app:dashboard')

from django.contrib.auth.models import User
from .models import GeneralTable, DateTable, TimeTable, PriceTable

@login_required
def listing_application_view(request, listing_id):
    try:
        listing_detail = ListingData.objects.get(pk=listing_id)
    except ListingData.DoesNotExist:
        raise Http404("Listing does not exist")

    listing_general_data = GeneralTable.objects.filter(listing_foreign_key=listing_detail)
    listing_date_data = DateTable.objects.filter(listing_foreign_key=listing_detail)
    listing_time_data = TimeTable.objects.filter(listing_foreign_key=listing_detail)
    listing_price_data = PriceTable.objects.filter(listing_foreign_key=listing_detail)

    context = {'listing_detail': listing_detail,
    'listing_general_data': listing_general_data,
    'listing_date_data': listing_date_data,
    'listing_time_data': listing_time_data,
    'listing_price_data': listing_price_data,}
    return render(request, 'main_app/listing_application.html', context=context)

from .forms import GeneralTableForm
from .models import GeneralTable

@login_required
def add_into_general_table(request):
    if request.method == 'POST':
        form = GeneralTableForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_app:dashboard'))
    else:
        form = GeneralTableForm()

    return render(request, 'main_app/add_into_general_table.html', {'form':form})

@login_required
def read_or_update_in_general_table(request, general_data_id):
    try:
        general_data = GeneralTable.objects.get(pk=general_data_id)
    except GeneralTable.DoesNotExist:
        return redirect('main_app:dashboard')
    form = GeneralTableForm(request.POST or None, instance = general_data)
    if form.is_valid():
       form.save()
       return redirect('main_app:dashboard')
    return render(request, 'main_app/read_or_update_in_general_table.html', {'form':form, 'data': general_data})

@login_required
def delete_in_general_table(request, general_data_id):
    try:
        general_data = GeneralTable.objects.get(pk=general_data_id)
    except GeneralTable.DoesNotExist:
        return redirect('main_app:dashboard')
    general_data.delete()
    return redirect('main_app:dashboard')

from .serializers import ListingDataSerializer, ListingUserGroupSerializer
from .serializers import GeneralTableSerializer, DateTableSerializer, TimeTableSerializer, PriceTableSerializer
from rest_framework import generics
from .models import ListingUserGroup
from .models import GeneralTable, DateTable, TimeTable, PriceTable


class ListingDataList(generics.ListCreateAPIView):
    queryset = ListingData.objects.all()
    serializer_class = ListingDataSerializer

class ListingDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingData.objects.all()
    serializer_class = ListingDataSerializer

class ListingUserGroupList(generics.ListCreateAPIView):
    queryset = ListingUserGroup.objects.all()
    serializer_class = ListingUserGroupSerializer

class ListingUserGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingUserGroup.objects.all()
    serializer_class = ListingUserGroupSerializer

class GeneralTableList(generics.ListCreateAPIView):
    queryset = GeneralTable.objects.all()
    serializer_class = GeneralTableSerializer

class GeneralTableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralTable.objects.all()
    serializer_class = GeneralTableSerializer

class DateTableList(generics.ListCreateAPIView):
    queryset = DateTable.objects.all()
    serializer_class = DateTableSerializer

class DateTableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DateTable.objects.all()
    serializer_class = DateTableSerializer

class TimeTableList(generics.ListCreateAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

class TimeTableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

class PriceTableList(generics.ListCreateAPIView):
    queryset = PriceTable.objects.all()
    serializer_class = PriceTableSerializer

class PriceTableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceTable.objects.all()
    serializer_class = PriceTableSerializer