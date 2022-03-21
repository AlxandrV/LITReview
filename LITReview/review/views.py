from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home(request):
    return render(request,
                  'review/home.html')

@login_required
def posts_user(request):
    return render(request,
                  'review/posts.html')

@login_required
def create_ticket(request):
    return render(request,
                  'review/create-ticket.html')