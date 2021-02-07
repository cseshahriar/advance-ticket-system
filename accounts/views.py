import logging
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# from django.contrib.auth.mixins import PermissionRequiredMixin
from tickets.models import Ticket

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