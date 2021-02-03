from django.shortcuts import render
from django.views.generic.edit import CreateView 
from . models import Priority, Category, Color, Ticket, Attachment
from . forms import TicketForm, AttachmentForm

class HomeView(CreateView):
    model = Ticket
    template_name = 'tickets/create.html'
    form_class = TicketForm
    formset_class = None
    success_url = '/'

    def get_context_data(self, **kwargs):
        pass 

    def form_valid(self, form):
        pass 
