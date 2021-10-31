
from django.views.generic import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardView(TemplateView,LoginRequiredMixin):
    template_name = "dashboard.html"

class ThanksView(TemplateView):
    template_name = "thanks.html"

class HomeView(TemplateView):
    template_name = "index.html"
    
    