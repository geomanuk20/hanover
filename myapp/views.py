from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_backends
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomAuthenticationForm,updateForm, PropertyForm,PropertyLocationForm,PropertyProfileForm,PropertyDetailsForm,PropertyImageForm
from .models import Property
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

User = get_user_model()

def home(request):
    if request.user.is_authenticated:
        user_properties = Property.objects.filter(user=request.user)
    else:
        user_properties = Property.objects.all()  # or a public subset

    return render(request, 'index.html', {'properties': user_properties})

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate and login the user
            user = authenticate(
                request,
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                password=form.cleaned_data['password1']
            )
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, phone=phone, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('home')
        messages.error(request, "Invalid email/phone or password.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            
            # Generate token and uid
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Create reset link
            reset_url = request.build_absolute_uri(
                f'/resetPassword/{uid}/{token}/'
            )
            
            # Send email
            send_mail(
                'Password Reset Request',
                f'Click this link to reset your password: {reset_url}',
                'noreply@yourdomain.com',
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Password reset link has been sent to your email.')
            return redirect('forgotPassword')
            
        except User.DoesNotExist:
            messages.error(request, 'No account found with this email address.')
    
    return render(request, 'forgotPassword.html')

def reset_password_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        
        if not default_token_generator.check_token(user, token):
            messages.error(request, 'Invalid or expired reset link.')
            return redirect('forgotPassword')
            
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password has been reset successfully. You can now login with your new password.')
                return redirect('login')
        else:
            form = SetPasswordForm(user)
            
        return render(request, 'resetPassword.html', {'form': form})
        
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        messages.error(request, 'Invalid reset link.')
        return redirect('forgotPassword')

def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('home')

# Other views remain the same
def testimonials(request):
    return render(request, 'testimonials.html')

def propertysale(request):
    if request.user.is_authenticated:
        user_properties = Property.objects.filter(user=request.user, transaction_type='sale')
    else:
        user_properties = Property.objects.filter(transaction_type='sale')  # Show all sale listings

    return render(request, 'propertysale.html', {'properties': user_properties})

def propertyRent(request):
    if request.user.is_authenticated:
        user_properties = Property.objects.filter(user=request.user, transaction_type='rent')
    else:
        user_properties = Property.objects.filter(transaction_type='rent')  # Show all sale listings
    return render(request, 'propertyRent.html',{ 'properties': user_properties })

def propertyPremium(request):
    return render(request, 'propertyPremium.html')

def finance(request):
    return render(request, 'finance.html')

def propertyoverview(request, id):
    property = get_object_or_404(Property, id=id)
    property.views += 1
    property.save()
    return render(request, 'propertyoverview.html', {'property': property})


def postProperty(request):
    return render(request, 'postProperty.html')

def postRequirement(request):
    return render(request, 'postRequirement.html')

def contactUs(request):
    return render(request, 'contactUs.html')

def ourService(request):
    return render(request, 'ourService.html')



def myAccount(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to view your account.")
        return redirect('login')
    
    user = request.user
    return render(request, 'myAccount.html', {'user': user})

# def myProperty(request):
#     if not request.user.is_authenticated:
#         messages.error(request, "You need to be logged in to view your properties.")
#         return redirect('login')
    
#     user = request.user
#     # Assuming you have a Property model related to the user
#     properties = user.property_set.all()  # Adjust according to your model relationships
#     return render(request, 'myProperty.html', {'user': user, 'properties': properties})

def my_property_view(request):
    user_properties = Property.objects.filter(user=request.user)
    return render(request, 'myProperty.html', {'properties': user_properties})

def edit_property(request, id):
    property_instance = Property.objects.get(id=id, user=request.user)
    
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Property updated successfully.")
            return redirect('myProperty')
    else:
        form = PropertyForm(instance=property_instance)
    
    return render(request, 'edit_property.html', {'form': form, 'property': property_instance})

def delete_property(request, id):
    property_instance = Property.objects.get(id=id, user=request.user)
    
    if request.method == 'POST':
        property_instance.delete()
        messages.success(request, "Property deleted successfully.")
        return redirect('myProperty')
    
    return render(request, 'delete_property.html', {'property': property_instance})


def myRequirement(request):
    return render(request, 'myRequirement.html')

def manageMedia(request,id):
    property = get_object_or_404(Property, id=id, user=request.user)
    
    context = {
        'property': property,
    }
    
    return render(request, 'manageMedia.html', context)
def paymentHistory(request):
    return render(request, 'paymentHistory.html')
def myWatchlist(request):
    return render(request, 'myWatchlist.html')
# def profile(request):
#     return render(request, 'profile.html')
def update_profile(request):
    if request.method == 'POST':
        form = updateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()  # Saves all fields automatically
            return redirect('myAccount')
    else:
        form = updateForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form})


def post_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            property_obj = form.save(commit=False)
            property_obj.user = request.user  # ← ForeignKey set here
            property_obj.save()
            return redirect('propertyBasicInfo')  # replace with your redirect
    else:
        form = PropertyForm()
    
    return render(request, 'postProperty.html', {'form': form})

def propertyBasicInfo(request, id):
    try:
        property_instance = Property.objects.get(id=id, user=request.user)
        
        if request.method == 'POST':
            form = PropertyForm(request.POST, instance=property_instance)
            if form.is_valid():
                property = form.save(commit=False)
                property.user = request.user
                
                # Handle price range logic
                if property.set_price == 'no':
                    property.price_range = None
                
                property.save()
                messages.success(request, "Property updated successfully!")
                return redirect('locationDetail', id=property.id)  # Redirect to a location or detail view
            else:
                # Debug form errors
                print("Form errors:", form.errors)
                messages.error(request, "Please correct the errors below.")
        else:
            form = PropertyForm(instance=property_instance)
        
        context = {
            'property': property_instance,
            'form': form
        }
        return render(request, 'propertyBasicInfo.html', context)
        
    except Property.DoesNotExist:
        messages.error(request, "Property not found or you don't have permission.")
        return redirect('myProperty')
    
def locationDetail(request, id):
    # Get the property or return 404 if not found or doesn't belong to user
    property_instance = get_object_or_404(Property, id=id, user=request.user)
    
    if request.method == 'POST':
        form = PropertyLocationForm(request.POST, instance=property_instance)
        if form.is_valid():
            # Save the form data
            property = form.save(commit=False)
            
            # Handle any additional logic before saving
            if not property.latitude or not property.longitude:
                # Set default coordinates if not provided
                property.latitude = 10.8505  # Default Kerala latitude
                property.longitude = 76.2711  # Default Kerala longitude
            
            property.save()
            messages.success(request, "Location details updated successfully!")
            return redirect('propertyProfile', id=property.id)  # Redirect to next step
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        # Initialize form with existing data
        form = PropertyLocationForm(instance=property_instance)
    
    context = {
        'property': property_instance,
        'form': form
    }
    return render(request, 'locationDetail.html', context)

def propertyProfile(request, id):
    property_instance = get_object_or_404(Property, id=id, user=request.user)
    
    if request.method == 'POST':
        form = PropertyProfileForm(request.POST, instance=property_instance)
        if form.is_valid():
            form.save()
            # Redirect to propertyDetail with the same property ID
            return redirect(reverse('propertyDetail', kwargs={'id': id}))
    else:
        form = PropertyProfileForm(instance=property_instance)
    
    context = {
        'form': form,
        'property': property_instance
    }
    return render(request, 'propertyProfile.html', context)

def propertyDetail(request, id):
    property_instance = get_object_or_404(Property, id=id, user=request.user)
    
    if request.method == 'POST':
        form = PropertyDetailsForm(request.POST, instance=property_instance)
        if form.is_valid():
            property = form.save(commit=False)
            # Convert empty strings to None
            property.bedrooms = form.cleaned_data['bedrooms'] or None
            property.bathrooms = form.cleaned_data['bathrooms'] or None
            property.save()
            # Redirect to propertyDetail with the same property ID
            return redirect(reverse('propertyImage', kwargs={'id': id}))
    else:
        form = PropertyDetailsForm(instance=property_instance)
    
    context = {
        'form': form,
        'property': property_instance
    }
    return render(request, 'propertyDetail.html', context)

def propertyImage(request, id):
    property_instance = get_object_or_404(Property, id=id, user=request.user)
    
    if request.method == 'POST':
        form = PropertyImageForm(request.POST, request.FILES, instance=property_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Property images updated successfully!")
            return redirect('myProperty')  # Redirect back to same page
    else:
        form = PropertyImageForm(instance=property_instance)
    
    # Get all existing images
    images = [
        {'field': 'image1', 'url': property_instance.image1.url if property_instance.image1 else None},
        {'field': 'image2', 'url': property_instance.image2.url if property_instance.image2 else None},
        {'field': 'image3', 'url': property_instance.image3.url if property_instance.image3 else None},
        {'field': 'image4', 'url': property_instance.image4.url if property_instance.image4 else None},
        {'field': 'image5', 'url': property_instance.image5.url if property_instance.image5 else None},
    ]
    
    context = {
        'form': form,
        'property': property_instance,
        'images': images,
    }
    return render(request, 'propertyImage.html', context)