from django.shortcuts import render
from django.views.generic.edit import CreateView 
from . models import Priority, Category, Color, Ticket, Attachment
from . forms import TicketForm, AttachmentFormSet
from django.http import HttpResponseRedirect
from django.contrib import messages


class HomeView(CreateView):
    model = Ticket
    template_name = 'tickets/create.html'
    form_class = TicketForm
    success_url = '/'
    object = None

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the
        form and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        attachment_form = AttachmentFormSet()
        return self.render_to_response(
            self.get_context_data(form=form, attachment_form=attachment_form,)
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        attachment_form = AttachmentFormSet(self.request.POST)
        if form.is_valid() and attachment_form.is_valid():
            return self.form_valid(form, attachment_form)
        else:
            return self.form_invalid(form, attachment_form)
    
    def form_valid(self, form, attachment_form):
        """
        Called if all forms are valid. Creates Assignment instance along with the
        associated AssignmentQuestion instances then redirects to success url
        Args:
            form: TicketForm
            attachment_form: attachment_form 

        Returns: an HttpResponse to success url
        """
        self.object = form.save(commit=False)
        # pre-processing for Assignment instance here...
        self.object.save()

        # saving AssignmentQuestion Instances
        attachments = attachment_form.save(commit=False)
        for attachment in attachments:
            #  change the AssignmentQuestion instance values here
            # attachments.ticket = self.get_object()
            attachment.save()

        messages.success(self.request, 'Ticket has been created.')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, attachment_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.

        Args:
            form: TicketForm
            attachments: attachment_form
        """
        return self.render_to_response(
            self.get_context_data(form=form, attachment_form=attachment_form)
        )
