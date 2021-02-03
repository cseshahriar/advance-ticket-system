from django.forms import ModelForm
from . models import Ticket, Attachment


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'priority', 'category', 'color', 'first_name', 'last_name',
            'middle_name', 'subject', 'description', 'email', 'phone', 
        ]

        
class AttachmentForm(ModelForm):
    class Meta:
        model = Attachment
        fields = ['ticket', 'attachment']
