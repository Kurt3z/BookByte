from django.contrib import admin

from .models import Publisher, Content, Country, Genre, District, City

admin.site.register(Publisher)
admin.site.register(Content)
admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(District)
admin.site.register(City)
