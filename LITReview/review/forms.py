from cProfile import label
from django import forms

from review.models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        labels = {
            'title': 'Titre',
        }
        exclude = ('user', 'time_created')