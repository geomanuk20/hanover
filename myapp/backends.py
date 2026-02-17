from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

class EmailOrPhoneAuthBackend(ModelBackend):
    def authenticate(self, request, email=None, phone=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Normalize phone number by removing all non-digit characters
            if phone:
                phone = ''.join(filter(str.isdigit, phone))
                
            # Find user by email or normalized phone number
            user = UserModel.objects.get(
                Q(email=email) if email else Q(phone__endswith=phone[-10:])  # Last 10 digits
            )
            
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        except UserModel.MultipleObjectsReturned:
            # Handle case where multiple users have the same email/phone
            return None
        except Exception as e:
            print(f"Authentication error: {str(e)}")
            return None