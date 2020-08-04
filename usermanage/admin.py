from django.contrib import admin
from .models import TUser, TAdmin, MainControl

admin.site.register(TUser)

admin.site.register(TAdmin)

admin.site.register(MainControl)

# Register your models here.
