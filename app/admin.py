from django.contrib import admin
from app.models import Profile,Property,Tenant
# Register your models here.
admin.site.register(Property)
admin.site.register(Tenant)
admin.site.register(Profile)