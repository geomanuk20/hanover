from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField
from django.conf import settings 
from django.utils import timezone

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
    customertype = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    landline = models.CharField(max_length=15, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

class Property(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # ✅ Correct way
    language = models.CharField(max_length=20)
    property_type = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=50)
    ownership_type = models.CharField(max_length=50)
    set_price = models.CharField(max_length=5, choices=[('yes', 'Yes'), ('no', 'No')])
    price_range = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, default="Untitled Property")
    property_description = models.TextField()
    proximity = models.TextField(blank=True, null=True)
    country = models.CharField(max_length=100, default='India')
    state = models.CharField(max_length=100, default='Kerala')
    district = models.CharField(max_length=100, null=True, blank=True)
    town = models.CharField(max_length=100,null=True, blank=True)
    locality = models.CharField(max_length=100,null=True, blank=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile1 = models.CharField(max_length=15, blank=True, null=True)
    mobile2 = models.CharField(max_length=15, blank=True, null=True)
    mobile3 = models.CharField(max_length=15, blank=True, null=True)
    landline1 = models.CharField(max_length=15, blank=True, null=True)
    landline2 = models.CharField(max_length=15, blank=True, null=True)
    landline3 = models.CharField(max_length=15, blank=True, null=True)
    plot_area = models.CharField(max_length=50, blank=True, null=True)
    plot_area_unit = models.CharField(max_length=20, choices=[('sqft', 'Square Feet'), ('sqm', 'Square Meters')], default='sqft')
    gated_property = models.BooleanField(default=False)
    residential_colony = models.BooleanField(default=False)
    bathrooms = models.CharField(max_length=10)
    bedrooms = models.CharField(max_length=10)
    image1 = CloudinaryField('image', blank=True, null=True)
    image2 = CloudinaryField('image', blank=True, null=True)
    image3 = CloudinaryField('image', blank=True, null=True)
    image4 = CloudinaryField('image', blank=True, null=True)
    image5 = CloudinaryField('image', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    posted_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.property_type} - {self.user}"
    