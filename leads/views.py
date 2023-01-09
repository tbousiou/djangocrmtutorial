from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from leads.models import Lead

# Create your views here.

class LeadListView(ListView):
    model = Lead
    context_object_name = 'leads'

class LeadDetailView(DetailView):
    model = Lead
    context_object_name = 'lead'

class LeadCreateView(CreateView):
    model = Lead
    template_name = "leads/lead_create.html"
    fields = ['first_name', 'last_name', 'agent']

class LeadUpdateView(UpdateView):
    model = Lead
    fields = ['first_name', 'last_name', 'agent']

# def lead_list(request):
#     return render(request, "leads/lead_list.html")