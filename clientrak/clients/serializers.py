from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Agent, Client, Trip
from datetime import timedelta

class SimpleTimeSerializer(serializers.TimeField):
    """
    Simply turn a timedelta into a number of seconds
    rather than a string representation
    """
    def to_representation(self, value):
        return value.total_seconds()

    def to_internal_value(self, value):
        return timedelta(seconds=value)

class AgentSerializer(serializers.ModelSerializer):
    activities = serializers.StringRelatedField(many=True)

    class Meta:
        model = Agent
        fields = ['user', 'minimum_rate', 'activity_types']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_first_name', 'client_last_name', 'agent']


class TripSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    time_spent = SimpleTimeSerializer()

    def create(self, validated_data):
        agent = Agent.objects.get(user=self.context['request'].user)
        client_data = validated_data.pop('client')
        client, _ = Client.objects.get_or_create(**client_data)
        trip = Trip.objects.create(client=client, **validated_data)

        return trip

    def update(self, instance, validated_data):
        client_data = validated_data.pop('client')
        client, _ = Client.objects.get_or_create(**client_data)
        instance.client = client
        instance.trip_name = validated_data.get('trip_name', instance.trip_name)
        instance.commission = validated_data.get('commission', instance.commission)
        instance.time_spent = validated_data.get('time_spent', instance.time_spent)

        instance.save()

        return instance

    class Meta:
        model = Trip
        fields = ['trip_name', 'commission', 'time_spent', 'client', 'id']
        depth = 1

