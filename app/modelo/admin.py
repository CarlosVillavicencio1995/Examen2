from django.contrib import admin

from .models import Usuario

class AdminUsuario(admin.ModelAdmin):
    list_display = ["cedula", "apellidoPaterno","apellidoMaterno", "Sexo", "nombres","estado"]
    list_editable = ["apellidoPaterno","apellidoMaterno","Sexo", "nombres"]
    search_fields = ["cedula"]

    class Meta:
        model = Usuario

admin.site.register(Usuario, AdminUsuario)
