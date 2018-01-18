from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

urlpatterns=[
url(r'^$',views.avail_times,name='avail_times'),
url(r'^login/$',views.Login_view.as_view(),name="login"),
url(r'^Dashboard.html$',views.dashboard),
url(r'^logout/$', views.Logout.as_view(), name='logout')]
