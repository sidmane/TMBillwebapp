from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,TemplateView
from .models import TmbinTable
from tmbill import settings
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dashboard(request):
    if request.user.is_authenticated:
        return render_to_response('Dashboard.html')
    else:
        return HttpResponseRedirect('login')

def avail_times(request):
    tables = TmbinTable.objects.all()
    return render_to_response('login.html', {'tables': tables})


def my_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponse('Dashboard.html')

class Login_view(TemplateView):

    """
    Login user code
    """

    def get(self, request):
        if request.user.is_active:
            return HttpResponseRedirect('/webapp/Dashboard.html')
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            print("yes")
            return HttpResponseRedirect('/webapp/Dashboard.html')
        else:
            return HttpResponse(status=400)


class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)
