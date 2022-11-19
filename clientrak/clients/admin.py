from django.contrib import admin
from django.db import models
from django.forms.widgets import TimeInput

from .models import Agent, Client, Trip, ActivityType, Activity

# Register your models here.

admin.site.register(Agent)
admin.site.register(ActivityType)
admin.site.register(Client)
admin.site.register(Trip)
admin.site.register(Activity)
