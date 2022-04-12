from itertools import chain
from multiprocessing import context
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import View
from django.views.generic.list import ListView
from django.db.models import Q

from review.models import Ticket, Review, UserFollows
from review.forms import TicketForm, ReviewForm

@login_required
def home(request):
    return render(request,
                  'review/home.html')

@login_required
def posts_user(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-time_created')
    reviews = Review.objects.filter(user=request.user).order_by('-time_created')
    records = sorted(chain(tickets, reviews), key=lambda date: date.time_created)
    return render(request,
                  'review/posts.html',
                  context={
                      'records': records,})

@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('home')
    else:
        form = TicketForm()
    return render(request,
                  'review/create-ticket.html',
                  {'form': form})
    
class DetailTicket(DetailView):
    ticket_model = Ticket
    review_model = Review
    
    def get(self, request, id):
        ticket = self.ticket_model.objects.get(id=id)
        reviews = self.review_model.objects.filter(ticket=ticket).order_by('-time_created')[:10]
        return render(request,
                  'review/detail-ticket.html',
                  context={'ticket': ticket, 'reviews': reviews})
        
class EditTicket(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'review/update-ticket.html'
    success_url = 'detail-ticket'
    
    def get_success_url(self):
        return reverse_lazy(self.success_url, kwargs={'id': self.object.id})
            
class DeleteTicket(DeleteView):
    model = Ticket
    template_name = 'review/delete-ticket.html'
    success_url = reverse_lazy('posts')

class ReviewFormView(View):
    form_class = ReviewForm
    template_name = 'review/create-review.html'
    success_url = 'review/detail-ticket.html'
    
    def get(self, request, id):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})
        
    def post(self, request, id):
        form = self.form_class(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            ticket = Ticket.objects.get(id=id)
            review.ticket = ticket
            review.save()
        return render(request,
                      self.success_url,
                      context={'ticket': ticket})

@login_required
def new_review(request):
    if request.method == 'POST':
        rform = ReviewForm(request.POST, prefix='rform')
        tform = TicketForm(request.POST, request.FILES, prefix='tform')
        if rform.is_valid() and tform.is_valid():
            ticket = tform.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = rform.save(commit=False)
            review.user = request.user
            last_ticket = Ticket.objects.last()
            review.ticket = last_ticket
            review.save()
            return redirect('detail-ticket', id=last_ticket.id)
    else:
        rform = ReviewForm(prefix='rform')
        tform = TicketForm(prefix='tform')

        # title = request.POST.get("title")
        # print(title)
    return render(request,
                  'review/new-review.html', 
                  context={'rform': rform, 'tform': tform})
    
class FollowsList(ListView):
    template_name = 'review/follows.html'
    
    def get(self, request):
        user_followeds = UserFollows.objects.filter(user=request.user)
        user_follow = UserFollows.objects.filter(followed_user=request.user)
        return render(request,
                      self.template_name,
                      context={
                          'followed': user_followeds,
                          'follow': user_follow})

@login_required
def search_follows(request):
    if request.method == 'POST':
        value = request.POST.get('search-value')
        followeds = UserFollows.objects.filter(user=request.user)
        users = User.objects.filter(Q(username__contains=value) & ~Q(id__in=[follow.followed_user.id for follow in followeds]))
        return render(request,
                      'review/users-list.html',
                      context={'users': users})

@login_required
def add_follow(request):
    if request.method == 'POST':
        id_user = request.POST.get('id-user')
        user_follow = User.objects.get(id=id_user)
        followed = UserFollows.objects.create(user=request.user, followed_user=user_follow)
        return render(request,
                      'review/followed-user.html',
                      context={'user': user_follow})
@login_required
def unfollow(request):
    if request.method == 'POST':
        id_user_unfollow = request.POST.get('id-user')
        user_unfollow = User.objects.get(id=id_user_unfollow)
        unfollow = UserFollows.objects.filter(user=request.user, followed_user=user_unfollow).delete()
        return JsonResponse({'delete': user_unfollow.id})