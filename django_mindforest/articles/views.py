from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'articles/home.html', {'title': 'Test'},)

def about(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'articles/about.html', context,)