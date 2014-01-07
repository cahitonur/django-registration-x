from django.conf.urls import patterns, url
from registration.dashboard.views import DashBoardMainView


urlpatterns = patterns('',
                       url(r'^$', DashBoardMainView.as_view(), name='dashboard-main'),
                       )