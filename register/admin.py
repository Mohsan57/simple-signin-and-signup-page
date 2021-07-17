from django.contrib import admin
from register.models import Register
# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_name',)
    list_filter = ('email', )
    prepopulated_fields = {'slug': ('user_name', )}
    search_fields = ('user_name',)


admin.site.register(Register, RegisterAdmin)
