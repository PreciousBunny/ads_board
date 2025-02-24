from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager as BaseUserManager
from django.apps import apps
from django.utils.translation import gettext_lazy as _


# Create your models here.
# здесь должен быть менеджер для модели Юзера.
# Поищите эту информацию в рекомендациях к проекту


class UserManager(BaseUserManager):
    """
    Класс переопределение модели для команды python manage.py createsuperuser
    (для поля email).
    """
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Function created and save a user with the given username, email,
        and password.
        """

        if not email:
            raise ValueError(_("The given username must be set"))
        email = self.normalize_email(email)
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        email = GlobalUserModel.normalize_username(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self._create_user(email, password, **extra_fields)
