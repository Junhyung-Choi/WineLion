from django.contrib import admin

from .models import *
# Register your models here.
admin.site.register(Wine)
admin.site.register(Review)
admin.site.register(Event)
admin.site.register(CustomUser)
admin.site.register(Food)