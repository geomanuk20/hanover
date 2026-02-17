from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgotPassword/', views.forgot_password_view, name='forgotPassword'),  # Password reset
    path('resetPassword/<uidb64>/<token>/', views.reset_password_view, name='reset_password'),
    path('logout/', views.logout_view, name='logout'),


    path('testimonials/', views.testimonials, name='testimonials'),  # Testimonials page
    path('propertysale/', views.propertysale, name='propertysale'),  # Property sale page
    path('propertyRent/', views.propertyRent, name='propertyRent'),  # Property rent page
    path('propertyoverview/<int:id>/', views.propertyoverview, name='propertyoverview'),# Property overview page
    path('propertyPremium/', views.propertyPremium, name='propertyPremium'),  # Premium properties page
    path('finance/', views.finance, name='finance'),  # Finance page
    path('postProperty/', views.post_property, name='postProperty'),  # Post property page
    path('propertyBasicInfo/', views.propertyBasicInfo, name='propertyBasicInfo'),  # Property basic info page
    path('postRequirement/', views.postRequirement, name='postRequirement'),  # Post requirement page
    path('contactUs/',views.contactUs, name='contactUs'),  # Contact Us page
    path('ourService/', views.ourService, name='ourService'),  # Our Services page


    path('myAccount/', views.myAccount, name='myAccount'),  # My Account page
    path('myProperty/', views.my_property_view, name='myProperty'),  # My Property Listings page
    path('locationDetail/<int:id>/', views.locationDetail, name='locationDetail'),  # Location detail page
    path('propertyProfile/<int:id>/', views.propertyProfile, name='propertyProfile'),  # Property profile page
    path('propertyDetail/<int:id>/', views.propertyDetail, name='propertyDetail'),  # Property detail page
    path('propertyImage/<int:id>/', views.propertyImage, name='propertyImage'),  # Property image upload page
    path('property/<int:id>/', views.propertyBasicInfo, name='property_detail'),
    path('property/edit/<int:id>/', views.edit_property, name='edit_property'),
    path('property/delete/<int:id>/', views.delete_property, name='delete_property'),
    path('myRequirement/', views.myRequirement, name='myRequirement'),  # My Requirements page
    path('manageMedia/', views.manageMedia, name='manageMedia'),  # Manage Media page
    path('paymentHistory/', views.paymentHistory, name='paymentHistory'),  # Payment History page
    path('myWatchlist/', views.myWatchlist, name='myWatchlist'),  # My Watchlist page
    path('profile/', views.update_profile, name='profile'),  # Profile page
     path('update-profile/',views.update_profile, name='update_profile'),
] 