import logging
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from tickets.models import Ticket, Attachment
from .forms import TicketForm, AttachmentFormSet

logger = logging.getLogger(__name__)

class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """ Dashboard Overview """
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'accounts/dashboard.html'
    # permission_required = ('polls.view_choice', 'polls.change_choice')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['obj'] = model.objects.all() 
        logger.info('Dashboard Overview')
        return context


class TicketsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    """ Tickets List View """

    model = Ticket
    paginate_by = 10
    template_name = 'accounts/tickets/list.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tickets'] = Ticket.objects.all().order_by('-pk')
        return context 

class TicketUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ticket
    template_name = 'accounts/tickets/update.html'
    form_class = TicketForm
    success_url = '/accounts/tickets/list'
    object = None

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the
        form and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        attachment_form = AttachmentFormSet(
            queryset=Attachment.objects.filter(
                ticket=self.get_object()
            )
        )
        return self.render_to_response(
            self.get_context_data(form=form, attachment_form=attachment_form,)
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        attachment_form = AttachmentFormSet(
            self.request.POST, self.request.FILES,
            queryset=Attachment.objects.filter(
                ticket=self.get_object()
            )
        )

        if form.is_valid() and attachment_form.is_valid():
            logger.info(f'ticket form validate')
            return self.form_valid(form, attachment_form)
        else:
            logger.error(f'ticket form validation errors')
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
        self.object = form.save()
        logger.info(f'Ticket updated id:{self.object.pk}')

        # attachment_form
        # attachments = attachment_form.save(commit=False)
        # for attachment in attachments:
        #     attachment.ticket = self.object
        #     attachment.save()
        #     logger.info(f'Ticket Attachments updated')
        attachment_form.save()
        messages.success(self.request, 'Ticket has been updated.')
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



def ticket_status_update(request):
    pass