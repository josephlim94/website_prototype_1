
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import ListingData

def index(request):
    template = loader.get_template('main_app/index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

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
@login_required
def listing_application_view(request, listing_id):
    try:
        listing_detail = ListingData.objects.get(pk=listing_id)
    except ListingData.DoesNotExist:
        raise Http404("Listing does not exist")
    user_list = User.objects.all()
    return render(request, 'main_app/listing_application.html', {'listing_detail': listing_detail, 'user_list': user_list})

from .serializers import ListingDataSerializer, GeneralTableSerializer, DateTableSerializer, TimeTableSerializer, PriceTableSerializer
from rest_framework import generics
from .models import GeneralTable, DateTable, TimeTable, PriceTable


class ListingDataList(generics.ListCreateAPIView):
    queryset = ListingData.objects.all()
    serializer_class = ListingDataSerializer

class ListingDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListingData.objects.all()
    serializer_class = ListingDataSerializer

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