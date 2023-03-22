from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy
from .manager import CustomUserManager
# Create your models here.


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    Full_name = models.CharField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=260)
    is_staff = models.BooleanField(
        gettext_lazy('staff'),
        default = False,
        help_text = gettext_lazy('Designetes whether the user can log in this site')
    )

    is_active = models.BooleanField(
        gettext_lazy('active'),
        default = True,
        help_text = gettext_lazy('Designetes whether the user should be created as active. Ulselect insted of deleting accounts')
    )
    join_date = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    
    
    objects = CustomUserManager()
    
    def __str__(self) -> str:
        return self.email
    
    
    def get_full_name(self):
        return self.email
    
    
    def get_short_name(self):
        return self.email
    
    class Meta:
        verbose_name = 'User'
        
