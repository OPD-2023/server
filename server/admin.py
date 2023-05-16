from django.contrib import admin

from server.models import Partner, Direction, Product, Service, History, SubService

# Register your models here.
admin.site.register(Product)
admin.site.register(Partner)
admin.site.register(Direction)
admin.site.register(Service)
admin.site.register(SubService)
admin.site.register(History)
