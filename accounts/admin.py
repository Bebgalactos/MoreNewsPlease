from django.contrib import admin
from .models import UserCustomised, EmailConfirmationModel
# Register your models here.
admin.site.register(UserCustomised)
admin.site.register(EmailConfirmationModel)