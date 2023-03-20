from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from Benches.models import Park

# Create your models here.

# we need to create the custom user model that actually stores the admin's
# information, and then a custom user manager that will be used to create
# the instances of these admin users

class CustomAdminUser(AbstractUser):
    """
    The custom user model holding the admin's information.
    """
    # we make use of the user's email as their username
    username = models.EmailField(unique=True, null=True, blank=True)  # you can't have two users with the same email
    # password is not set as a field here for security reasons
    ### NOTE: to need to modify this reference to the park application next
    manages_park = models.ForeignKey(Park, on_delete=models.CASCADE, null=True, blank=True)
    # on deletion of a park, the admin managing it gets deleted 

    # superuser permissions
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # set email as the username field
    USERNAME_FIELD = "username"
    # set the required fields for the user creation
    REQUIRED_FIELDS = []  # none 

    def __str__(self):
        return f"Admin {self.id} - {self.username}"

    def has_perm(self, perm, obj=None):
        # since our only users are either superusers (John) or not (regular admins)
        # we can just return the superuser status
        return self.is_superuser

    def has_module_perms(self, app_label):
        # only superusers should be able to access the admin panel
        return self.is_superuser

class CustomAdminUserManager(BaseUserManager):
    """
    The custom user manager used to create/manage instances of the custom
    user model for admins.
    """

    # default custom creation for users based on email and password
    def create_user(self, username, password, **extra):
        if not username:
            raise ValueError("Valid email is required")
        if not password:
            raise ValueError("Valid password is required")
        
        # keep in mind the password is the one created automatically by the
        # user creation view, so it will never be None

        # create the user with the provided email and other fields
        user = self.model(username=self.normalize_email(username), **extra)

        # set the password for the user
        user.set_password(make_password(password))
        user.save(using=self._db)
        return user  # return user id 
    
    def create_superuser(self, username, password, **extra):
        # create a superuser with the provided email and password (using normal creation)
        user = self.create_user(username=username, password=password, **extra)
        # grant superuser permissions
        user.is_superuser = True
        user.is_staff = True
        # get rid of username as an attrbute
        user.username = None
        # save the modified user
        user.save(using=self._db)
        return user