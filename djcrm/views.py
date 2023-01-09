from django.views.generic import TemplateView


class LandindPageView(TemplateView):
    template_name = 'landing-page.html'