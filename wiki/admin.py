from django.contrib import admin

from wiki.models import WikiPost, WikiCategory

# Register your models here.

@admin.register(WikiPost)
class WikiAdmin(admin.ModelAdmin):
    #pass
    list_display = ('wiki_title', 'wiki_favorite', 'wiki_status', )
    list_filter = ('wiki_status', )
    search_fields = ('wiki_content', )

@admin.register(WikiCategory)
class WikiCategoryAdmin(admin.ModelAdmin):
    #pass
    list_display = ('category_name', )
