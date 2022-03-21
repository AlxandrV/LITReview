from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request,
                  'review/home.html')
    
def posts_user(request):
    return render(request,
                  'review/posts.html')