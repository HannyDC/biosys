import flet as ft 
import airtable as at

def main(page: ft.Page):
    #Configuracion de la pagina
    page.title = "Consulta"
    page.theme_mode = "light"
    page.window.width = 500
    page.window.height = 650
    page.appbar = ft.AppBar(
        title= ft.Text("Consulta de Usuario en la Nube"),
        leading= ft.Icon("cloud"),
        center_title=True,
        bgcolor= "pink",
        color= "white"
    )
    #Table de Usuario
    encabezado = [
        ft.DataColumn(ft.Text("Clave")),
        ft.DataColumn(ft.Text("Contraseña")),
        ft.DataColumn(ft.Text("Nombre Completo")),
        ft.DataColumn(ft.Text("Es Administrador"))
    ]
    filas = []
    datos = at.usuario.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.clave))
        celda2 = ft.DataCell(ft.Text(d.contra, color="white", selectable=True))
        celda3 = ft.DataCell(ft.Text(d.nombre))
        celda4 = ft.DataCell(ft.Text(d.admin))
        fila = ft.DataRow([celda1,celda2,celda3,celda4])
        filas.append(fila)

    tbl_usuario = ft.DataTable(encabezado,filas)

    page.add(tbl_usuario)
    page.update()


if __name__=="__main__":
    ft.app(target=main)