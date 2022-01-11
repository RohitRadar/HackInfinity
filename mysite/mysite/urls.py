from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('camera',views.cam, name="cam"),
    path('terminal',views.term, name="term"),
    path('alerts',views.alert, name="alert"),
]
