from django.contrib import admin

from bookmark.models import BookmarkPost, BookmarkCategory

# Register your models here.

@admin.register(BookmarkPost)
class BookmarkAdmin(admin.ModelAdmin):
    #pass
    list_display = ('bookmark_title', 'bookmark_favorite', 'bookmark_status', 'bookmark_category')
    list_filter = ('bookmark_status', )
    search_fields = ('bookmark_title', )

@admin.register(BookmarkCategory)
class BookmarkCategoryAdmin(admin.ModelAdmin):
    #pass
    list_display = ('category_name', )
