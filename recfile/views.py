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

class TimeFreeRecore_Create(FormView):
    form_class = TimeFreeRecordForm

    def form_valid(self, form):
        radiko = Radiko()
        (radiko_file, prog_data) = radiko.record_timefree_rec09(form.cleaned_data['channel'], form.cleaned_data['t_ft'].replace(tzinfo=None), form.cleaned_data['t_to'].replace(tzinfo=None))
        Recfile.objects.create(
            prog_title = prog_data['title'],
            prog_channel = prog_data['channel'],
            prog_id = prog_data['id'],
            prog_ft = prog_data['ft'],
            prog_to = prog_data['to'],
            prog_dur = (prog_data['to'] - prog_data['ft']).seconds,
            prog_url = prog_data['url'],
            prog_desc = prog_data['desc'],
            prog_info = prog_data['info'],
            prog_pfm = prog_data['pfm'],
            prog_img = prog_data['img'],
            prog_hashtag = prog_data['hashtag'],
            prog_file = radiko_file
        )
        
        return render(self.request, 'recorded.html', {'form': form})
