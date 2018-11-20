
from django.contrib import admin
from django.urls import path
from Don_portfolio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about,name='about'),
    path('post/<int:pk>/', views.workview, name='workview'),
    path('contact', views.contact, name='contact'),
    path('', views.home,name='home'),
    path('Portraits',views.Portraits,name='Portraits'),
    path('illustrations',views.illustrations,name='illustrations'),
    path('successView',views.successView,name='successView')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
