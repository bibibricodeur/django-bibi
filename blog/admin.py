from django.contrib import admin

from .models import BlogPost, BlogCategory

# Register your models here.

# https://docs.djangoproject.com/fr/3.1/intro/tutorial07/

@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    #pass
    list_display = ('blog_title', 'blog_favorite', 'blog_status')
    list_filter = ('blog_status', )
    search_fields = ('blog_content', )

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    #pass
    list_display = ('category_name', )
