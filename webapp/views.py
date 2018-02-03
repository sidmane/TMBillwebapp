from django.shortcuts import render, render_to_response,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import View,TemplateView
from .models import TmbinTable,TmbinCustomer
from tmbill import settings
from django.urls import reverse_lazy
from django.contrib.auth import logout,authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import (ListView, DetailView,
                                  UpdateView, DeleteView, CreateView, View)


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def dashboard(request):
    if request.user.is_authenticated:
        tables = TmbinTable.objects.all()
        return render_to_response('Dashboard.html',{'tables': tables})
    else:
        return HttpResponseRedirect('login')

def showCustomer(request):
    if request.user.is_authenticated:
        customers = TmbinCustomer.objects.all()
        return render_to_response('masters/customerManagement.html',{'customers':customers})
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


class Customer_Details(DetailView):
    model=TmbinCustomer
    template_name="masters/customers/customer_details.html"
    context_object_name = "customer"

class Customer_List(ListView):
    model=TmbinCustomer
    template_name = "masters/customers/customer_list.html"
    context_object_name = "customerslist"

    def get_queryset(self):
        query = self.request.GET.get('search_product')
        if query:
            return TmbinCustomer.objects.all()
        else:
            return TmbinCustomer.objects.all()

class Customer_save(CreateView):

    '''
    product save
    '''

    model = TmbinCustomer
    template_name = "masters/customers/customer_save.html"
    fields = ['name','mobile','email','business_name','address','gst_no','description']
    success_url = reverse_lazy("webapp:customer_list")

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(Customer_save, self).form_valid(form)

class Customer_delete(DeleteView):


    model = TmbinCustomer
    success_url = reverse_lazy("webapp:customer_list")

class Customer_edit(UpdateView):

    model = TmbinCustomer
    template_name = "masters/customers/customer_edit.html"
    fields = ['name','mobile','email','business_name','address','gst_no','description']
    success_url = reverse_lazy("webapp:customer_list")
