from django import forms
from .models import TmbinCustomer

class customerForm(forms.ModelForm)
    class Meta:
        model=TmbinCustomer
        fields=('name','mobile','email','business_name','address','gst_no','description')
