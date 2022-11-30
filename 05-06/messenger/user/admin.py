from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id',  'username')
    list_filter = ('id',)

admin.site.register(User, UserAdmin)

