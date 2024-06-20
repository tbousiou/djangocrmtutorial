from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Lead

# Create your views here.

class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    context_object_name = 'leads'

class LeadDetailView(LoginRequiredMixin, DetailView):
    model = Lead
    #context_object_name = 'lead'

class LeadCreateView(LoginRequiredMixin, CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    fields = ['first_name', 'last_name', 'age', 'agent']

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    model = Lead
    template_name = "leads/lead_update.html"
    fields = ['first_name', 'last_name', 'age', 'agent']

class LeadDeleteView(LoginRequiredMixin, DeleteView):
    model = Lead
    template_name = "leads/lead_delete.html"
    success_url = reverse_lazy('leads:lead-list')

