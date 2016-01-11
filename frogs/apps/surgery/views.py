from django.shortcuts import render

from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, \
    ListView, UpdateView, TemplateView, View

from surgery.forms import SurgeryForm
from surgery.models import Surgery

class SurgeryCreate(CreateView):
    model = Surgery
    form_class = SurgeryForm
    success_url = '/'

class SurgeryDelete(DeleteView):
    model = Surgery
    success_url = '/'

class SurgeryDetail(DetailView):
    model = Surgery

class SurgeryList(ListView):
    model = Surgery
    
class SurgeryUpdate(UpdateView):
    model = Surgery
    form_class = SurgeryForm
    success_url = '/'

    
