from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from .models import Post



def index(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'index.html',context)    