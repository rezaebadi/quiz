from django.contrib import admin
from .models import (
    Author, Book, Company, Employee, Photo, Post,
    Profile, Survey, Tag, Taggeditem, Tenant
)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author')
    search_fields = ('title',)
    list_filter = ('author',)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company')
    search_fields = ('name',)
    list_filter = ('company',)

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_path')
    search_fields = ('file_path',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    search_fields = ('title',)
    list_filter = ('is_published',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'bio')
    search_fields = ('user__username', 'bio')

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('id', 'questions_json')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Taggeditem)
class TaggeditemAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag', 'content_type', 'object_id')
    list_filter = ('tag', 'content_type')

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'schema_name')
    search_fields = ('schema_name',)
