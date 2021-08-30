"""basketballLeague URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from league import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name='team-detail'),
    path('players/', views.PlayerList.as_view()),
    path('players/<int:pk>/', views.PlayerDetail.as_view(), name='player-detail'),
    path('leagues/', views.LeagueList.as_view()),
    path('leagues/<int:pk>/', views.LeagueDetail.as_view(), name='league-detail'),
    path('rounds/', views.RoundList.as_view()),
    path('rounds/<int:pk>/', views.RoundDetail.as_view(), name='round-detail'),
    path('games/', views.GameList.as_view()),
    path('games/<int:pk>/', views.GameDetail.as_view(), name='game-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)