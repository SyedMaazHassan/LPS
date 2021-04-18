from django.shortcuts import render, redirect
from .models import *
from application.supporting_func import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
# Create your views here.

def index(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("registration:index")

    account_of_user = get_account_type(request.user)
    if account_of_user['status'] == "client":
        return render(request, 'dashboard/client/index.html', context)
    else:
        return redirect("registration:index")