from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "registration"
urlpatterns = [
    path('', views.index, name="index"),
    path('lawyer', views.lawyer_registration, name="lawyer"),
    path('createLawyer', views.createLawyer, name="createLawyer"),
    path('client', views.client_registration, name="client"),
    path('createClient', views.createClient, name="createClient")
    # path('register-as-lawyer', views.register_as_lawyer, name="register-as-lawyer"),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
