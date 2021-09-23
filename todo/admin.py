from django.contrib import admin

from todo.models import TodoPost, TodoCategory

# Register your models here.

@admin.register(TodoPost)
class TodoAdmin(admin.ModelAdmin):
    #pass
    list_display = ('todo_title', 'todo_completed', 'todo_favorite', 'todo_status')
    list_filter = ('todo_status', )
    search_fields = ('todo_title', )

@admin.register(TodoCategory)
class TodoCategoryAdmin(admin.ModelAdmin):
    #pass
    list_display = ('category_name', )
