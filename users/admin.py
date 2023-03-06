from django.contrib import admin

# 이걸 import해서 userAdmin을 사용해야함
# admin.Modeladmin을 쓰면 커스텀이 아닌 기본 설정을 쓰는 것!!
# 그러므로 반드시 아래를 임포트 해서 커스ㅓ마이징해야함
from django.contrib.auth.admin import UserAdmin
from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username", "password", "name", "email", "is_host",),
                "classes":("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes":("collapse",),
            },
        ),
        (
            "Importat Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes":("collapse",),
            },
        ),
    )
    # fields = ("email","password","name")
    list_display = ("username","email","name","is_host",)

    pass
