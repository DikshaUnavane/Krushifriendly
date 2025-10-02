from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'price', 'specifications', 'image']
    
    # Adding widgets for better styling
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Equipment Name'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price'}))
    specifications = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Specifications', 'rows': 3}), required=False)
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))


from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


# app/forms.py
from django import forms
from .models import Renter

class RenterForm(forms.ModelForm):
    class Meta:
        model = Renter
        fields = ['name', 'phone', 'email']  # latitude and longitude will be captured automatically
