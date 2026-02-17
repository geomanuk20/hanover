from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm
from .models import CustomUser
from .models import Property

class CustomUserCreationForm(UserCreationForm):
    # email = forms.EmailField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ("username", "email", "phone", "password1","password2")

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("email","phone", "password")


class updateForm(UserChangeForm):
    # Exclude the password field
    password = None

    class Meta:
        model = CustomUser
        fields = [
            'email', 
            'phone', 
            'name', 
            'profile_picture', 
            'customertype', 
            'address', 
            'city', 
            'state', 
            'country', 
            'district', 
            'landline'
        ]

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'language',
            'property_type',
            'transaction_type',
            'ownership_type',
            'set_price',
            'price_range',
            'property_description',
            'proximity',
        ]
        widgets = {
            'property_description': forms.Textarea(attrs={
                'rows': 5,
                'minlength': 50,
                'maxlength': 2000,
                'required': True
            }),
            'proximity': forms.Textarea(attrs={
                'rows': 3,
                'maxlength': 500
            }),
            'price_range': forms.TextInput(attrs={
                'placeholder': 'e.g., 50,00,000 - 60,00,000'
            })
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price_range'].required = False
        self.fields['proximity'].required = False
        
        # Set initial choices for fields
        self.fields['language'].choices = [
            ('english', 'English'),
            ('malayalam', 'Malayalam')
        ]
        
        self.fields['property_type'].choices = [
            ('residential-apartment', 'Residential Apartment'),
            ('residential-house', 'Residential House/Villa'),
            ('residential-land', 'Residential Land'),
            ('residential-other', 'Residential Other'),
            ('commercial-building', 'Commercial Building'),
            ('commercial-other', 'Commercial Other'),
            ('industrial-building', 'Industrial Building'),
            ('commercial-shop', 'Commercial Shop'),
            ('agricultural-land', 'Agricultural Land')
        ]
        
        self.fields['transaction_type'].choices = [
            ('sale', 'Sale'),
            ('rent', 'Rent'),
            ('lease', 'Lease')
        ]
        
        self.fields['ownership_type'].choices = [
            ('freehold', 'Freehold'),
            ('leasehold', 'Leasehold')
        ]
        
        self.fields['set_price'].choices = [
            ('yes', 'Yes'),
            ('no', 'No (Price on Request)')
        ]


class PropertyLocationForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'country', 'state', 'district', 'town', 
            'locality', 'street', 'latitude', 'longitude'
        ]
        
        widgets = {
            'country': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'town': forms.Select(attrs={'class': 'form-control'}),
            'locality': forms.Select(attrs={'class': 'form-control'}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }

class PropertyProfileForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'email', 'mobile1','mobile2','mobile3' ,'landline1', 'landline2', 'landline3'
        ]
        
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile1': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile2': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile3': forms.TextInput(attrs={'class': 'form-control'}),
            'landline1': forms.TextInput(attrs={'class': 'form-control'}),
            'landline2': forms.TextInput(attrs={'class': 'form-control'}),
            'landline3': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PropertyDetailsForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'plot_area', 'plot_area_unit', 
            'gated_property', 'residential_colony','bedrooms', 'bathrooms'
        ]
        
        widgets = {
            'plot_area': forms.TextInput(attrs={'class': 'form-control'}),
            'plot_area_unit': forms.Select(attrs={'class': 'form-control'}),
            'gated_property': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'residential_colony': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'bedrooms': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
            'bathrooms': forms.TextInput(attrs={'class': 'form-control', 'min': 0}),
        }

class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['image1', 'image2', 'image3', 'image4', 'image5']
        widgets = {
            'image1': forms.FileInput(attrs={'class': 'form-control'}),
            'image2': forms.FileInput(attrs={'class': 'form-control'}),
            'image3': forms.FileInput(attrs={'class': 'form-control'}),
            'image4': forms.FileInput(attrs={'class': 'form-control'}),
            'image5': forms.FileInput(attrs={'class': 'form-control'}),
        }