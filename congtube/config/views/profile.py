from django.views.generic.base import TemplateView


class ProfileView(TemplateView):
    template_name = 'users/profile.html'
