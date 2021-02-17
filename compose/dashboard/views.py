# Django
from django.views.generic import FormView, TemplateView


class HomeView(TemplateView):

    template_name = 'dashboard/home_view.html'
