from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, firstname, password=None):
        if not email:
            raise ValueError("L'utilisateur doit avoir un email")
        if not username:
            raise ValueError("L'utilisateur doit avoir un nom d'utilisateur")
        
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            firstname=firstname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, firstname, password):
        user = self.create_user(username, email, firstname, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return self.email

    # ✅ Ajoute ces méthodes pour éviter l'erreur
    def has_perm(self, perm, obj=None):
        return True  # Permet toutes les permissions (à affiner)

    def has_module_perms(self, app_label):
        return True