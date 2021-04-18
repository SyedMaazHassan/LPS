from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, auth
from django.forms.models import model_to_dict
# Create your models here.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver

class lawyer_plan(models.Model):
    price = models.FloatField()
    sublowers_allowed = models.IntegerField()

    def __str__(self):
        return f'${self.price} - {self.sublowers_allowed} people'


class lawyer(models.Model):
    """

    Model for lawyer registration

    """
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number =  models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    lisence_number = models.CharField(max_length=90) #ask for limit
    bar_number = models.CharField(max_length=90)
    selected_plan = models.ForeignKey(lawyer_plan, on_delete = models.CASCADE)
    is_approved = models.BooleanField(default = False) #True #False
    is_rejected = models.BooleanField(default = False) #False #True
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(default = datetime.now())
    is_sublawyer = models.BooleanField(default = False)
    profile_pic = models.ImageField(upload_to="lawyerprofile", null = True)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_details(self):
        my_plan = model_to_dict(self.selected_plan)
        my_date_format = self.joined_at.strftime('%d %b, %Y - %I:%M %p')
        my_dict_data = model_to_dict(self)
        my_dict_data['joined_at'] = my_date_format
        my_dict_data['selected_plan'] = my_plan
        return my_dict_data

class client(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number =  models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    joined_at = models.DateTimeField(default = datetime.now())
    profile_pic = models.ImageField(upload_to="clientprofile", null = True)