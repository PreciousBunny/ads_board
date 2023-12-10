from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from users.models import User


# Aдмика для пользователя - как реализовать ее можно подсмотреть в документаци django
# Обычно её всегда оформляют, но в текущей задачи делать её не обязательно
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone',
                    'is_active', 'is_staff', 'is_superuser', 'role',)
    list_filter = ('id', 'is_active', 'role',)
