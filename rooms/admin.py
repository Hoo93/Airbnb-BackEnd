from django.contrib import admin
from .models import Room, Amenities

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Amenities)
class AmenityAdmin(admin.ModelAdmin):
    pass
