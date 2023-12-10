from django.contrib import admin
from ads.models import Ad, Comment


# здесь можно подкючить ваши модели к стандартной джанго-админке
# Register your models here.


@admin.register(Ad)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'description', 'price',
                    'image', 'created_at',)
    list_filter = ('title', 'price',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'author', 'ad', 'created_at',)
    list_filter = ('text', 'author',)
