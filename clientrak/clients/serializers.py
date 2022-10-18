from rest_framework import serializers
from .models import Agent, Client, Trip

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['first_name', 'last_name', 'minimum_rate']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_first_name', 'client_last_name', 'agent']
        depth = 1

class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ['trip_name', 'commission', 'time_spent', 'client']
        depth = 1

