from django.urls import path
from django.conf.urls import url
from . import views as core_views
from django.contrib.auth import views as auth_views

from . import views

app_name = 'main_app'
urlpatterns = [
    # ex: /main_app/
    path('', views.index, name='index'),
    # ex: /main_app/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /main_app/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /main_app/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]
