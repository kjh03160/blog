from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.utils import timezone

from .models import Post

def home(request):
    posts = Post.objects.order_by('-date')

    context = {
        'posts' : posts,
    }

    return render(request, 'home.html', context)