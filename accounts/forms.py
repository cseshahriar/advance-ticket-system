from django.forms import ModelForm
from django.forms.models import modelformset_factory
from tickets.models import Ticket, Attachment
from django.forms import HiddenInput


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

AttachmentFormSet = modelformset_factory(
    Attachment,
    form=AttachmentForm,
    extra=1,
    can_delete=True
)
