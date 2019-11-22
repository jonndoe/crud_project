from django.views.generic import ListView, DetailView


from .models import Crudobject


class CrudobjectListView(ListView):
    model = Crudobject
    context_object_name = 'crudobject_list'
    template_name = 'crudobjects/crudobject_list.html'


class CrudobjectDetailView(DetailView):
    model = Crudobject
    context_object_name = 'crudobject'
    template_name = 'crudobjects/crudobject_detail.html'