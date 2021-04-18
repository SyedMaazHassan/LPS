from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json
from application.supporting_func import *
# Create your views here.

def index(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("registration:index")

    account_of_user = get_account_type(request.user)
    if account_of_user['status'] == "lawyer":
        return render(request, 'dashboard/lawyer/index.html', context)
    else:
        return redirect("registration:index")
    