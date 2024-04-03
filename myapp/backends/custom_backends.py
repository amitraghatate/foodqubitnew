from django.contrib.auth.backends import ModelBackend
from myapp.models import UserProfile
from django.contrib.auth.hashers import check_password

class UserProfileModelBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(email=email)

            if check_password(password, user.password):
                return user
        except UserProfile.DoesNotExist:
            return None