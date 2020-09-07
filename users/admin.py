from django.contrib import admin
from . import models

# Register your models here.

# admin.site.register(models.User, CustomUserAdmin) 과 같은 기능을 함
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """ Custom User Admin """

    # admin 페이지에서 모델의 속성이 보임
    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")
