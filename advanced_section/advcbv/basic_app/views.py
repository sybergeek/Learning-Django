from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                  ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView)
from . import models
from django.urls import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    # school_list returned by default

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail' # school returned by default
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
