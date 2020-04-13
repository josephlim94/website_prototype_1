from django.urls import path
from django.conf.urls import url
from . import views as core_views
from django.contrib.auth import views as auth_views

from . import views

from organizations.views import OrganizationCreate

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    path('listing_application_view/<int:listing_id>/', views.listing_application_view, name='listing_application_view'),
    path('listing_data/', views.ListingDataList.as_view(), name='listing_data'),
    path('listing_data/<int:pk>/', views.ListingDataDetail.as_view()),
    path('general_table/', views.GeneralTableList.as_view(), name='general_table'),
    path('general_table/<int:pk>/', views.GeneralTableDetail.as_view()),
    path('date_table/', views.DateTableList.as_view(), name='date_table'),
    path('date_table/<int:pk>/', views.DateTableDetail.as_view()),
    path('time_table/', views.TimeTableList.as_view(), name='time_table'),
    path('time_table/<int:pk>/', views.TimeTableDetail.as_view()),
    path('price_table/', views.PriceTableList.as_view(), name='price_table'),
    path('price_table/<int:pk>/', views.PriceTableDetail.as_view()),
    path('organization_create/', OrganizationCreate.as_view(), name='organization_create'),
    path('add_into_general_table/', views.add_into_general_table, name='add_into_general_table'),
]
