from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookinAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "room",
        "experience",
        "check_in",
        "check_out",
        "experience_time",
        "gusests",
    )

    list_filter = (
        "kind",
        "check_in",
        "experience_time",
    )
