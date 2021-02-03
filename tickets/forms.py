from django.forms import ModelForm
from django.forms.models import inlineformset_factory
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


AttachmentFormSet = inlineformset_factory(Ticket,
    Attachment,
    fields=['attachment'],
    # set to false because cant' delete an non-exsitant instance
    can_delete=False,
    extra=1
)
