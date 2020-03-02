from django.contrib import admin

# Register your models here.
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']

admin.site.register(SubCategory, SubCategoryAdmin)

class CommentInline(admin.StackedInline):
    model = Comment

class TaskAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = ['title', 'category', 'subcategory', 'source', 'status', 'user', 'w_link', 'trello_board_name' , 'content', 'is_active', 'is_trello_exported']
    list_filter = ('category', 'subcategory', 'status')
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'task', 'file', 'user', 'trello_id','is_support']

admin.site.register(Comment, CommentAdmin)


class LogAdmin(admin.ModelAdmin):
    list_display = ['name', 'desc']

admin.site.register(Log, LogAdmin)

