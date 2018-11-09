from django.contrib import admin


from .models import Estudiantes
class AdminEstudiante(admin.ModelAdmin):
    list_display = ["cedula", "nombres", "apellidos",  "genero"]
    list_editable = ["apellidos", "nombres"]
    list_filter = ["apellidos", "genero"]
    search_fields = ["cedula", "nombres", "apellidos"]

    class Meta:
        model= Estudiantes 

admin.site.register(Estudiantes, AdminEstudiante)