# Django
from django.views.generic import FormView


class HomeView(FormView):

    template_name = 'dashboard/home_view.html'