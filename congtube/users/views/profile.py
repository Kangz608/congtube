from django.views.generic.base import TemplateView


class ProfileView(TemplateView):
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['orders'] = self.request.user.order_set.is_display()
        return context
