from django.contrib import admin

from account.models import UserManager, User

admin.site.register(UserManager, User)

# Register your models here.
