from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    #Customize the list display
    list_display = ('title','author','publication_year')

    #Add search fields
    search_fields = ('title','author')

    #Add list filters
    list_filter = ('publication_year',)

# Register the Book model with the customized admin class
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm  # Define this form if needed
    form = CustomUserChangeForm  # Define this form if needed
    list_display = ('username', 'email', 'date_of_birth', 'profile_photo', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'date_of_birth', 'profile_photo'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)