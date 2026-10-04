
# Create your views here.
from django.shortcuts import render
from .models import Post

def home(request):

    posts = Post.objects.all()
    
    context = {
        'site_name': 'blogapp',
        'posts': posts}
    return render(request, 'home.html', context)

def about(request):
    context = {
        'title': 'About Page'
    }
    return render(request, 'about.html', context)