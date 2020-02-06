from django.contrib import admin
# from django_tenants.admin import TenantAdminMixin

# Register your models here.
from .models import DashboardConfig #, SmtpEmailSettings

class DashboardConfigAdmin(admin.ModelAdmin):
    # # This will help you to disbale add functionality
    def has_add_permission(self, request):
        try:
          return False if self.model.objects.count() > 0 else super().has_add_permission(request)
        except Exception as e:
          pass

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False

# class SmtpEmailSettingsAdmin(admin.ModelAdmin):
#     # # This will help you to disbale add functionality
#     def has_add_permission(self, request):
#         try:
#           return False if self.model.objects.count() > 0 else super().has_add_permission(request)
#         except Exception as e:
#           pass

#     # This will help you to disable delete functionaliyt
#     def has_delete_permission(self, request, obj=None):
#         return False

admin.site.register(DashboardConfig, DashboardConfigAdmin)
# admin.site.register(SmtpEmailSettings, SmtpEmailSettingsAdmin)