#from pyairtable import Api
from pyairtable.orm import Model
from pyairtable.orm import fields


class usuario(Model):
    clave = fields.TextField("clave")
    contra = fields.TextField("contra")
    nombre = fields.TextField("nombre")
    admin = fields.CheckboxField("admin")
    class Meta:
        api_key = "patddj75juQQctN64.640cb9e46f034de99df77e9f25843de1da99b34889974c2ef6bfe780ef604079"
        base_id = "app0792rIxoA7dOn3"
        table_name = "usuario"

class Bioenergia(Model):
    cultivo = fields.TextField("cultivo")
    parte = fields.TextField("parte")
    cantidad = fields.FloatField("cantidad")
    area = fields.FloatField("area")
    energia = fields.FloatField("energia")
    municipio = fields.SelectField("municipio")
    latitud = fields.FloatField("latitud")
    longitud = fields.FloatField("longitud")
    class Meta:
        api_key = "patddj75juQQctN64.640cb9e46f034de99df77e9f25843de1da99b34889974c2ef6bfe780ef604079"
        base_id = "app0792rIxoA7dOn3"
        table_name = "bioenergia"

cacao = Bioenergia(
    cultivo = "Cacao",
    parte = "Cascara",
    cantidad = 36.0,
    area = 12.3,
    energia = 20.2,
    municipio = "Paraíso",
    latitud = 18.076169,
    longitud = 17.904267
)

cacao.save()

#api = Api("patddj75juQQctN64.640cb9e46f034de99df77e9f25843de1da99b34889974c2ef6bfe780ef604079")
#tabla = api.table("app0792rIxoA7dOn3", "usuario")


#altas
#yo = {'clave': 'chavez',
#'contra': 'chavez',
#'nombre': 'Oscar chavez',
#'admin': 1
#}

#tabla.create(yo)

#registros = tabla.all()
#for r in registros:
#    print(r["fields"])