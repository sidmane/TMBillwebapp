from django.conf.urls import url
from . import views
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

app_name = 'webapp'
urlpatterns=[
url(r'^$',views.avail_times,name='avail_times'),
url(r'^login/$',views.Login_view.as_view(),name="login"),
url(r'^Dashboard.html$',views.dashboard),
url(r'^customerManagement/$', login_required(views.Customer_List.as_view()), name='customer_list'),
url(r'^customerManagement/new/$', login_required(views.Customer_save.as_view()), name='customer_save'),
url(r'^customerManagement/(?P<pk>\d+)/$',login_required(views.Customer_Details.as_view()),name='customer'),
url(r'^customerManagement/(?P<pk>\d+)/delete/$',login_required(views.Customer_delete.as_view()),name='customer_delete'),
url(r'^customerManagement/(?P<pk>\d+)/edit/$',login_required(views.Customer_edit.as_view()),name='customer_edit'),
url(r'^logout/$', views.Logout.as_view(), name='logout')]
