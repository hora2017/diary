from django.contrib import admin
from .models import Post

# Register your models here.

# class PostAdmin(admin.TabularInline):
#     fieldsets = [
#         ('data', {'fields':['created_date']}),
#     ]

# class PostAdmin(admin.ModelAdmin):
#     fields = ['created_date']

class PostAdmin(admin.ModelAdmin):
    list = ('created_date')

#admin.site.register(Post)
admin.site.register(Post, PostAdmin)