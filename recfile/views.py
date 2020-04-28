from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .models import Recfile

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class RadikoListView(ListView):
    model = Recfile
    template_name = "list.html"

    def queryset(self):
        return Recfile.objects.all()
