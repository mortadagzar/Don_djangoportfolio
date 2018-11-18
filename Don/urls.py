
from django.contrib import admin
from django.urls import path
from Don_portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

]
