from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = "application"
urlpatterns = [
    path('', views.index, name="index"),
    # path('register-as-lawyer', views.register_as_lawyer, name="register-as-lawyer"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('search-lawyers', views.searchlawyers, name="search-lawyers"),
    path('uploadImage', views.uploadImage, name="uploadImage")
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
