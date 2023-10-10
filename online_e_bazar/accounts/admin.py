from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserPayment, UserAddress, ShoppingSession
# from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['username', 'first_name', 'last_name', 'email', 'telephone', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('telephone',)}),)
#     add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('telephone',)}),)


# admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserAddress)
admin.site.register(ShoppingSession)
# admin.site.register(CartItem)
admin.site.register(UserPayment)




