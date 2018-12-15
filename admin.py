from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Lineitem)
admin.site.register(Nation)
admin.site.register(Orders)
admin.site.register(Part)
admin.site.register(Partsupp)
admin.site.register(Region)
admin.site.register(Supplier)
