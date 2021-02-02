from django.shortcuts import render
from django.views.generic.edit import CreateView 
from . models import Priority, Category, Color, Ticket, Attachment

class HomeView(CreateView):
    model = Ticket
    template_name = 'tickets/create.html'
    form_class = None
    formset_class = None
    success_url = '/'

    def get_context_data(self, **kwargs):
        pass 

    def form_valid(self, form):
        pass 
