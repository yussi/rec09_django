from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, TemplateView, FormView
from .models import Recfile
from .forms import TimeFreeRecordForm
from django.urls import reverse_lazy
from .radiko import Radiko

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class RadikoListView(ListView):
    model = Recfile
    template_name = "list.html"

    def queryset(self):
        return Recfile.objects.all()

class RadikoDetailView(DetailView):
    model = Recfile
    template_name = "detail.html"

class TimeFreeRecordFormView(FormView):
    form_class = TimeFreeRecordForm
    template_name = "timefreerecord.html"

class TimeFreeRecordForm_Confirm(FormView):
    form_class = TimeFreeRecordForm
    
    def form_valid(self, form):
        radiko = Radiko()
        prog = radiko.get_program_by_channel(form.cleaned_data['channel'], form.cleaned_data['t_ft'].replace(tzinfo=None))
        return render(self.request, 'timefreerecord_confirm.html', {'form': form, 'prog': prog})
