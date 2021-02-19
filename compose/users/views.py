# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class UserDetailView(LoginRequiredMixin, TemplateView):

    template_name = 'users/profile.html'
