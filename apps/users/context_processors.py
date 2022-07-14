<<<<<<< HEAD
from .models import User
=======
from .models import CustomUser
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86
from django.conf import settings
from django.db.models import Q

def all_profiles(request):
<<<<<<< HEAD
    all_profiles = User.objects.all()#.exclude(Q(user=request.user.profile))#| Q(id=settings.ANONYMOUS_USER) )
=======
    all_profiles = CustomUser.objects.all()#.exclude(Q(user=request.user.profile))#| Q(id=settings.ANONYMOUS_USER) )
>>>>>>> 78e8157e87090d617eb91c9d38cd1e4995547a86
    return {'all_profiles': all_profiles} # NOMBRE DEL OBJETO LLAMABLE DEBEN SER IGUALES