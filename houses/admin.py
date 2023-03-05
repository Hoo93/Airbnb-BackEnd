from django.contrib import admin
from .models import House

# Register your models here.
@admin.register(House)
# admin 할 모델이 House 라고 설명해줌
class HouseAdmin(admin.ModelAdmin):
    pass