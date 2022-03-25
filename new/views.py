from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Comment
import datetime
# Create your views here.

class DemoListView(ListView):
    model = Post
    template_name = 'home.html'

class DemoListView2(ListView):
    model = Post
    template_name = 'about.html'

class DemoListView3(ListView):
    model = Post
    template_name = 'services.html'

class DemoListView4(ListView):
    model = Post
    template_name = 'projects.html'

def DemoListView5(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone',None)
        email = request.POST.get('email',None)
        message = request.POST.get('message',None)
        user = Comment.objects.create(
            userName = name,
            phone = phone,
            email = email,
            message = message
        )
        user.save()
        print(message)
    return render(
    request=request,
    template_name = 'contact.html'
    )


class DemoListView6(ListView):
    model = Post
    template_name = 'learn.html'