from django.contrib import admin

from server.models import Partner, Direction, Product, Project, Service, History

# Register your models here.
admin.site.register(Product)
admin.site.register(Partner)
admin.site.register(Direction)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(History)
