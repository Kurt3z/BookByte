from django.contrib import admin

from .models import Contact, Reader, Librarian

admin.site.register(Contact)
admin.site.register(Reader)
admin.site.register(Librarian)
