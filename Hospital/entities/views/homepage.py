"""
This view contains the hompage view.
"""
from django.views.generic import (
    TemplateView,
    # ListView,
    # DetailView,
    # CreateView,
    # UpdateView,
    # DeleteView,
    # FormView,
)


class HomepageView(TemplateView):
    """This view is for the homepage"""
    template_name = 'index.html'
