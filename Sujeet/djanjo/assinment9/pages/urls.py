from django.urls import path
from django.urls.conf import include
from .views import upload
urlpatterns = [
    path('', upload, name='Home')
]