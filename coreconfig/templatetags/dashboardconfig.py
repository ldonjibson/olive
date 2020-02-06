from django import template

from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
from coreconfig.models import *

register = template.Library()


@register.simple_tag()
def DashboardConfigs():
	try:
		dashboardConfig = DashboardConfig.objects.all()
		return dashboardConfig[0]
	except Exception as e:
		return ''