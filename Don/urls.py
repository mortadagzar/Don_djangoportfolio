
from django.contrib import admin
from django.urls import path
from Don_portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('post/<int:pk>/', views.workview, name='workview'),
    path('contact', views.contact, name='contact'),
    path('home', views.home, name='home'),
    path('successView',views.successView,name='successView')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
