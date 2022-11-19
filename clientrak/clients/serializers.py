from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Agent, Client, Trip, Activity, ActivityType
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


class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = ['name']


class ActivityCRUDSerializer(serializers.ModelSerializer):
    time_spent = SimpleTimeSerializer()

    class Meta:
        model = Activity
        fields = ['trip', 'time_spent', 'act_type']

class ActivityNestedSerializer(serializers.ModelSerializer):
    act_type = serializers.StringRelatedField()

    class Meta:
        model = Activity
        fields = ['act_type', 'time_spent', 'create_date', 'updated_date']


class TripSerializer(serializers.ModelSerializer):
    client = ClientSerializer(many=False)
    time_spent = SimpleTimeSerializer(read_only=True)
    activities = ActivityNestedSerializer(many=True, read_only=True)

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

        instance.save()

        return instance

    class Meta:
        model = Trip
        fields = ['trip_name', 'commission', 'time_spent', 'client', 'activities', 'id']
        depth = 1


