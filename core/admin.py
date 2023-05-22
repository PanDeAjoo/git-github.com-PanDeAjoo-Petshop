from django.contrib import admin
from .models import *


class ProductoAdmin(admin.ModelAdmin):
    list_display  = ['nombre','descripcion','precio','stock','tipo']
    search_fields = ['nombre']
    list_per_page = 3

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductoAdmin)

