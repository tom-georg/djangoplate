from django.contrib import admin
from notesdemo.models import DemoNote
# Register your models here.

admin.site.site_header = "DjangoPlate Admin"

admin.site.register(DemoNote)