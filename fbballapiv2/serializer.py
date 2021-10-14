from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class CompiledTeamSerializer(serializers.Serializer):
    teamName = serializers.CharField(required=True)
    players = serializers.ListField(child=serializers.CharField(),required=True)

class LeagueSerializer(serializers.Serializer):
    teams = serializers.ListField(child=CompiledTeamSerializer(),required=True)

