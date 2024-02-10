from django.contrib import admin

from .models import Requisition


class RequisitionAdmin(admin.ModelAdmin):
    readonly_fields = ("date_created", "return_date")


admin.site.register(Requisition, RequisitionAdmin)
