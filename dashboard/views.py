from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from registration.models import Profile


class DashBoardMainView(TemplateView):
    template_name = 'registration/dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(DashBoardMainView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(DashBoardMainView, self).get_context_data(**kwargs)
        user = self.request.user
        profile = Profile.objects.get(user=user)
        profile_type = profile.profile_type
        context['user'] = user
        context['profile'] = Profile.objects.get(user=user)
        context['profile_type'] = profile_type

        return context