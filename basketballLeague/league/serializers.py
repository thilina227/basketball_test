from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class TeamSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    players = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='player-detail')

    class Meta:
        model = Team
        fields = ['id', 'name', 'players']

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    playerId = serializers.IntegerField(read_only=True)

    class Meta:
        model = Player
        fields = '__all__'

    def create(self, validated_data):
        return Player.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.height = validated_data('height', instance.height)
        instance.averageScore = validated_data('averageScore', instance.averageScore)
        instance.team = validated_data('team', instance.team)
        instance.save()
        return instance


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    leagueId = serializers.IntegerField(read_only=True)
    rounds = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='round-detail')

    class Meta:
        model = League
        fields = '__all__'

    def create(self, validated_data):
        return League.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class RoundSerializer(serializers.HyperlinkedModelSerializer):
    roundId = serializers.IntegerField(read_only=True)
    games = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='game-detail')

    class Meta:
        model = Round
        fields = '__all__'

    def create(self, validated_data):
        return Round.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.league = validated_data('league', instance.league)
        instance.save()
        return instance


class GameSerializer(serializers.HyperlinkedModelSerializer):
    gameId = serializers.IntegerField(read_only=True)

    class Meta:
        model = Game
        fields = '__all__'

    def create(self, validated_data):
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.round = validated_data.get('round', instance.round)
        instance.firstTeam = validated_data('firstTeam', instance.firstTeam)
        instance.secondTeam = validated_data('secondTeam', instance.secondTeam)
        instance.firstTeamScore = validated_data('firstTeamScore', instance.firstTeamScore)
        instance.secondTeamScore = validated_data('secondTeamScore', instance.secondTeamScore)
        instance.winningTeam = validated_data('winningTeam', instance.winningTeam)
        instance.save()
        return instance
