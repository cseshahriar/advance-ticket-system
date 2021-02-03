from django.contrib import admin
from . models import (Priority,Category, Color, Ticket, Attachment)


@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = (
        'id', 'name', 'code', 'is_active', 'created_at', 'updated_at',
    )
    list_display_links = ('name',)
    list_filter = ('created_at',)
    search_fields = ['name', 'code']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = (
        'id', 'title', 'slug', 'is_active', 'created_at', 'updated_at',
    )
    list_display_links = ('title',)
    list_filter = ('created_at',)
    search_fields = ('title',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'name', 'code', 'hex_code', 'is_active', 
                    'created_at', 'updated_at')
    list_display_links = ('name',)
    list_filter = ('created_at',)
    search_fields = ('name', 'code',)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'subject', 'priority', 'category', 'color', 
                    'is_active', 'created_at', 'updated_at')
    list_display_links = ('subject',)
    list_filter = ('priority', 'category', 'created_at')
    search_fields = ('subject', 'category', 'priority',)



@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'ticket', 'attachment', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('ticket',)
    list_filter = ('ticket', 'created_at')
    search_fields = ('ticket',)



