from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
# from django.contrib.auth.mixins import PermissionRequiredMixin

import logging
logger = logging.getLogger(__name__)

class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    
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