from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from home import views

urlpatterns = [
        path('',views.index,name ="home"),
        path('table1',views.show,name="table"),
        path('table2',views.show2,name="table2"),
        path('table3',views.show3,name="table3")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
