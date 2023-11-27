from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from users.managers import UserManager
# from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

# Create your models here.


NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    """
    Класс перечисления для выбора ролей пользователя.
    """
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractBaseUser):
    """
    Класс для работы с моделью User (пользователя).
    """
    username = None
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    role = models.CharField(max_length=15, choices=UserRoles.choices, default=UserRoles.USER, verbose_name='Роль')
    image = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_staff = models.BooleanField(default=False, verbose_name='Служебный персонал')
    is_superuser = models.BooleanField(default=False, verbose_name='Superuser')

    # Переопределение настроек для авторизации и регистрации через модель
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'role', 'image', ]

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        """
        Класс мета-настроек.
        """
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('email',)
