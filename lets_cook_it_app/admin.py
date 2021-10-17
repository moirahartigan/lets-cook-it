from django.contrib import admin
from .models import Categories, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Categories)
class CategoriesAdmin(SummernoteModelAdmin):

    summernote_fields = ('ingredients', 'method')


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'categories')
    list_display = ('title', 'categories', 'author', 'status', 'created_on')
    search_fields = ['title', 'ingredients', 'categories']
    summernote_fields = ('ingredients', 'method')
    actions = ['approve_recipes']

    def approve_approve_recipes(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'message', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'message')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
