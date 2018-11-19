from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from .models import Post

from django.shortcuts import get_object_or_404


def index(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'index.html',context)



def about(request):
    
    return render(request,'about.html')



def workview(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'workview.html', {'post': post})