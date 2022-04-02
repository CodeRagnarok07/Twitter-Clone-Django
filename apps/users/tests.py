from django.test import TestCase
from .models import User, Profile
# Create your tests here.

class ProfileTest(TestCase):
    """ testing for models"""
    def setUp(self): # Construye el objeto a verificar
        self.user = User.objects.create_user(
            first_name = "name",
            username ="name",
            email = "name@gmail.com",
            password = "name",
            )
        self.profile = Profile.objects.create(user=self.user)

    def test_Exp_model(self):
        self.assertTrue(isinstance(self.user, User))
        self.assertTrue(isinstance(self.profile, Profile))