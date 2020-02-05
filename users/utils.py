import requests
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.validators import RegexValidator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string


# Create your views here.
def get_or_none(Model, **kwarg):
    try:
        obj = Model.objects.get(**kwarg)
        return obj
    except ObjectDoesNotExist:
        return None

def get_or_filter(Model, **kwarg):
    try:
        obj = Model.objects.filter(**kwarg).exclude(api_name__icontains="DND")
        # if len(obj) == 0:
        return obj[0]
    except Exception as e:
        # raise e
        return None

