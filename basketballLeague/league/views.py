from rest_framework import generics
from .serializers import *
from .models import *


# Create your views here.

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def get_queryset(self):
        queryset = Player.objects.all()
        team = self.request.query_params.get('team')
        avg_score = self.request.query_params.get('avg_score')

        if team:
            queryset = queryset.filter(team=team)
        if avg_score:
            queryset = queryset.filter(averageScore__gte=avg_score)
        return queryset


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class LeagueList(generics.ListCreateAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class LeagueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer


class RoundList(generics.ListCreateAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class RoundDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
