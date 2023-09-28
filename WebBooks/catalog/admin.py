from django.contrib import admin
from .models import Author, Book, Genre, Language, Publisher, Status, BookInstance
from django.utils.html import format_html


# Определяем класс AuthorAdmin для авторов книг
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'data_of_birth', 'photo', 'show_photo')
    # fields = ['last_name', 'first_name', ('data_of_birth', 'photo')]
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style=max-height:100px;>'
        )
    show_photo.short_description = 'Фото'


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance


# Регистрируем класс BookAdmin для книг
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'language', 'display_author', 'show_photo')
    list_filter = ('genre', 'author')
    inlines = [BooksInstanceInline]
    readonly_fields = ['show_photo']

    def show_photo(self, obj):
        return format_html(
            f'<img src="{obj.photo.url}" style=max-height:100px;>'
        )
    show_photo.short_description = 'Обложка'


# Регистрируем класс BookinstanceAdmin для экземпляров книг
@admin.register(BookInstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_filter = ('book', 'status')
    fieldsets = (
        ('Экземпляр книги', {
            'fields': ('book', 'inv_nom')}),
        ('Статус и его окончание действий', {
            'fields': ('status', 'due_back')}),
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Status)
