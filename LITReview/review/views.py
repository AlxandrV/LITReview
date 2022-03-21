from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from review.models import Ticket
from review.forms import TicketForm

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
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request,
                  'review/create-ticket.html',
                  {'form': form})