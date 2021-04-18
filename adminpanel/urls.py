from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "adminpanel"
urlpatterns = [
    path('', views.index, name="index"),
    path('requests', views.lawyer_requests, name="requests"),
    path('getLawyer', views.get_lawyer, name="getLawyer"),
    path('requestoperation', views.requestoperation, name="requestoperation")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
