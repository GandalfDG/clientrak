from rest_framework import serializers
from django.contrib.auth.models import User
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
    client = ClientSerializer(many=False)

    def create(self, validated_data):
        agent = Agent.objects.get(user=self.context['request'].user)
        client_data = validated_data.pop('client')
        client, _ = Client.objects.get_or_create(agent=agent, **client_data)
        trip = Trip.objects.create(client=client, **validated_data)

        return trip

    class Meta:
        model = Trip
        fields = ['trip_name', 'commission', 'time_spent', 'client']
        depth = 1

