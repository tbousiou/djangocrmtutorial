from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from leads.models import Lead

# Create your views here.

class LeadListView(ListView):
    model = Lead
    context_object_name = 'leads'

class LeadDetailView(DetailView):
    model = Lead
    #context_object_name = 'lead'

class LeadCreateView(CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    fields = ['first_name', 'last_name', 'age', 'agent']

class LeadUpdateView(UpdateView):
    model = Lead
    template_name = "leads/lead_update.html"
    fields = ['first_name', 'last_name', 'age', 'agent']

class LeadDeleteView(DeleteView):
    model = Lead
    template_name = "leads/lead_delete.html"
    success_url = reverse_lazy('leads:lead-list')

