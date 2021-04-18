from django.shortcuts import render, redirect
from application.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
import json

total_plans = lawyer_plan.objects.all()

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("application:index")
    return render(request, "dashboard/choose.html")

def lawyer_registration(request):
    total_plans = lawyer_plan.objects.all()
    context = {
        "total_plans": total_plans
    }
    return render(request, "dashboard/register.html", context)

# Function to create lawyer
def createLawyer(request):
    total_plans = lawyer_plan.objects.all()
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')
        phone_number = request.POST.get('pnumber')
        address = request.POST.get('address')
        LicenseNumber = request.POST.get('lnumber')
        BarNumber = request.POST.get('barnumber')
        selectedPlan = request.POST.get('selectedPlan')

        context = {
            "fname" : fname,
            "lname": lname,
            "email" : email,
            "password" : password1, 
            "phone_number" : phone_number,
            "address" : address,
            "LicenseNumber" : LicenseNumber,
            "BarNumber" : BarNumber,
            "selectedPlan" : selectedPlan,
            "total_plans": total_plans
        }

        print(context)

        if password1==password2:
            if User.objects.filter(username=email).exists():
                print("Email already taken")
                messages.info(request, "Entered email already in use!")
                context['border'] = "my-email"
                return render(request, "dashboard/register.html", context)

            if not lawyer_plan.objects.filter(id = int(selectedPlan)).exists():
                print("Select a valid plan!")
                messages.info(request, "Select a valid plan!")
                context['border'] = "plan"
                return render(request, "dashboard/register.html", context)

            new_user = User.objects.create_user(username=email, first_name=fname, password=password1, last_name=lname)
            new_user.save()

            # create a lawyer separately
            new_lawyer = lawyer(
                first_name = fname,
                last_name = lname,
                email = email,
                phone_number = phone_number,
                address = address,
                lisence_number = LicenseNumber,
                bar_number = BarNumber,
                selected_plan = lawyer_plan.objects.get(id = int(selectedPlan)),
                user = new_user
            )
            new_lawyer.save()
            messages.info(request, "Your LAWYER account has been created!")
            return redirect("application:login")
        else:
            messages.info(request, "Your paswords does not match!")
            context['border'] = "my-passwords"
            return render(request, "dashboard/register.html", context)


    return redirect("registration:lawyer")
    


def client_registration(request):
    return render(request, "dashboard/registerClient.html")


# to create client separately
def createClient(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirmPassword')
        phone_number = request.POST.get('pnumber')
        address = request.POST.get('address')

        context = {
            "fname" : fname,
            "lname": lname,
            "email" : email,
            "password" : password1, 
            "phone_number" : phone_number,
            "address" : address,
        }

        print(context)

        if password1==password2:
            if User.objects.filter(username=email).exists():
                print("Email already taken")
                messages.info(request, "Entered email already in use!")
                context['border'] = "my-email"
                return render(request, "dashboard/registerClient.html", context)

            new_user = User.objects.create_user(username=email, first_name=fname, password=password1, last_name=lname)
            new_user.save()

            # create a lawyer separately
            new_client = client(
                first_name = fname,
                last_name = lname,
                email = email,
                phone_number = phone_number,
                address = address,
                user = new_user
            )
            new_client.save()
            messages.info(request, "Your CLIENT account has been created!")
            return redirect("application:login")
        else:
            messages.info(request, "Your paswords does not match!")
            context['border'] = "my-passwords"
            return render(request, "dashboard/registerClient.html", context)


    return redirect("registration:client")
    
