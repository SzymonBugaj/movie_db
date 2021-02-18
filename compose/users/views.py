from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import model_to_dict
from django.views.generic import TemplateView


class UserDetailView(LoginRequiredMixin, TemplateView):

    template_name = 'users/profile.html'