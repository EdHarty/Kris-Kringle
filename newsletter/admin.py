from django.contrib import admin
from .models import UserContact, NewsLetter


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name_surname', 'email', 'details',)

    search_fields = ('name_surname', 'email')


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'date', 'email',)

    search_fields = ('date', 'email',)


admin.site.register(NewsLetter, NewsletterAdmin)
admin.site.register(UserContact, ContactAdmin)
