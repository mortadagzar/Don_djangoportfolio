from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from .models import Post
from *forms import ContactForm

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




def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')    