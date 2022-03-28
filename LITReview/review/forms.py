from cProfile import label
from django import forms

from review.models import Ticket, Review

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        labels = {
            'title': 'Titre',
        }
        exclude = ('user', 'time_created')
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        labels = {
            'headline': 'Titre',
            'rating': 'Note',
            'body': 'Commentaire',
        }
        exclude = ('ticket', 'user', 'time_created')
