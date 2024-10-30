from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (
            None, {
                "fields":(
                    "username",
                    "password",
                )
            }   
        ),
        (
            "Informacion personal",{
                "fields":(
                    "email",
                    "dni",
                    "telefono",
                )
            }
        ),
        (
            "Permisos", {
                "fields":(
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            }
        ),
        (
            "fechas importantes", {
                "fields":(
                    "last_login",
                    "date_joined",
                )
            }
        ),
    )
     

