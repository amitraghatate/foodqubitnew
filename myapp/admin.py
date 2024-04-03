from django.contrib import admin
from .models import adminPanel

class adminPanelAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

admin.site.register(adminPanel, adminPanelAdmin)
