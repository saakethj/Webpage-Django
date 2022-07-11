from django.contrib import admin
from . models import Mobile, EarBuds


class MobileAdmin(admin.ModelAdmin):
    list_display = ('Brand', 'Model', 'Ram', 'Price')


class EarBudsAdmin(admin.ModelAdmin):
    list_display = ('Company', 'Model_Name', 'Version', 'Noise_Cancellation', 'Cost')


admin.site.register(Mobile, MobileAdmin)
admin.site.register(EarBuds, EarBudsAdmin)


