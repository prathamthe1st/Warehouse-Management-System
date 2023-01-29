from django.contrib import admin
from .models import sq, stock, prophet
# Register your models here.
admin.site.register(stock)
admin.site.register(sq)
admin.site.register(prophet)