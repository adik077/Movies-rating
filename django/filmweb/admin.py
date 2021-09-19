from django.contrib import admin
from .models import Film, DodatkoweInfo, Ocena,Aktor

#admin.site.register(Film)
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    search_fields = ["tytul","opis"]
    list_display = ["tytul","rok","imbq_rating"]
    list_filter = ["rok"]

admin.site.register(DodatkoweInfo)
admin.site.register(Ocena)
admin.site.register(Aktor)