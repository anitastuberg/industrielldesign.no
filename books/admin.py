from django.contrib import admin

from books.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ["__str__"]

    class Meta:
        model = Book


admin.site.register(Book, BookAdmin)