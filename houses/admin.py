from django.contrib import admin
from .models import House

# Register your models here.
@admin.register(House)
# admin 할 모델이 House 라고 설명해줌
class HouseAdmin(admin.ModelAdmin):
    
    # Column 구현
    fields = (
        "name",
        "address",
        ("price_per_night","pet_allowed"),
    )
    list_display = ("name","price_per_night","address","pet_allowed")
    list_filter = ("price_per_night","pet_allowed")
    search_fields = ("address__startswith",)
    list_display_links = ("name","address")
    list_editable = ("pet_allowed",)
    