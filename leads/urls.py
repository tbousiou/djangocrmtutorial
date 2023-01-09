from django.urls import path
from .views import LeadListView, LeadDetailView, LeadCreateView

app_name = 'leads'

urlpatterns = [
   path('', LeadListView.as_view(), name='lead-list'),
   path('<int:pk>', LeadDetailView.as_view(), name='lead-detail'),
   path('add', LeadCreateView.as_view(), name='lead-add')
]
