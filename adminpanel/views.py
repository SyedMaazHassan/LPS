from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import json
from application.supporting_func import *
# Create your views here.

def index(request):
    context = {}
    if not request.user.is_authenticated:
        return redirect("registration:index")
    
    account_of_user = get_account_type(request.user)
    if account_of_user['status'] == "admin":
        return render(request, 'dashboard/adminpanel/index.html', context)
    else:
        return redirect("registration:index")
  


# getting all lawyer requests
def lawyer_requests(request):
    if request.user.is_authenticated and request.user.is_superuser:
        context = {}
        context['all_requests'] = lawyer.objects.filter(is_approved = False, is_rejected = False).order_by("-id")
        context['all_approved'] = lawyer.objects.filter(is_approved = True).order_by("-id")
        context['all_rejected'] = lawyer.objects.filter(is_rejected = True).order_by("-id")
        return render(request, 'dashboard/adminpanel/lawyer-requests.html', context)
    return redirect("application:index")

# get lawyer details by id
def get_lawyer(request):
    output = {}
    if request.method == "GET" and request.is_ajax():
        lawyer_id = int(request.GET['id'])
        query = lawyer.objects.filter(id = lawyer_id) 
        if query.exists():
            output['status'] = True
            focused_lawyer = query[0]
            output["details"] = focused_lawyer.get_details()
            print(output['details'])
        else:
            output['status'] = False
            output['msg'] = "Lawyer doesn't exists"

    return JsonResponse(output)

def requestoperation(request):
    output = {}
    if request.method == "GET" and request.is_ajax():
        operation = request.GET['operation']
        Id = request.GET['id']
        try:
            query = lawyer.objects.filter(id = int(Id))
            if operation in ['accept', 'reject'] and query.exists():
                focused_lawyer = query[0]
                print(operation)
                print(Id)
                if operation == "accept":
                    output['msg'] = "Lawyer has been approved!"
                    focused_lawyer.is_approved = True
                    focused_lawyer.is_rejected = False
                else:
                    output['msg'] = "Lawyer has been rejected!"
                    focused_lawyer.is_approved = False
                    focused_lawyer.is_rejected = True

                focused_lawyer.save()
                output['status'] = True
            else:
                output['status'] = False
        except:
            output['status'] = False

    return JsonResponse(output)