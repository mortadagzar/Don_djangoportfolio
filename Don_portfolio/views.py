from django.http import HttpResponse
from django.shortcuts import render_to_response, render,redirect
from .models import Post
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

from django.shortcuts import get_object_or_404


def Portraits(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, 'Portraits.html',context)



def about(request):
    
    return render(request,'about.html')



def workview(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'workview.html', {'post': post})

def illustrations(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'illustrations.html',context)
    



def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['mortadagzar@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('successView')
    return render(request, "contact.html", {'form': form})

gffff ghghg gh

def successView(request):
    return render(request, "successView.html")



def home(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request, "home.html",context)

    