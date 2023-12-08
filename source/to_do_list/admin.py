from django.contrib import admin
from to_do_list.models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'description', 'created_at','detailed_description']
    list_display_links = ['id', 'status', 'description', 'created_at']
    list_filter = ['status']
    search_fields = ['id', 'status']
    fields = ['status', 'description', 'created_at','detailed_description']
    readonly_fields = ['created_at']

