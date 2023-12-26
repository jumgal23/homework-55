from django.contrib import admin
from to_do_list.models import Article, Status, Type, Project


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'status','type', 'description', 'detailed_description', 'created_at', 'updated_at']
    list_display_links = ['id', 'status', 'description', 'type']
    list_filter = ['status', 'type']
    search_fields = ['id', 'status', 'type']
    fields = ['status', 'type', 'description', 'detailed_description', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name']

@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']
    fields = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'start_date', 'end_date']
    list_display_links = ['id', 'name', 'description', 'start_date', 'end_date']
    search_fields = ['id', 'name', 'description', 'start_date', 'end_date']
    fields = ['name', 'description', 'start_date', 'end_date']
