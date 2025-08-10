import flet as ft
import airtable as at
import principal as pri

def main(page: ft.Page):

    def menu(e):
        page.clean()
        pri.main(page)

    # Configuración de la página
    page.title = "Consulta Bioenergía"
    page.theme_mode = "light"
    page.window_width = 800
    page.window_height = 700
    page.padding = 20
    page.horizontal_alignment = "center"

    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de Bioenergía en la Nube", style=ft.TextStyle(size=22, weight="bold")),
        leading=ft.Icon(name="cloud", size=30),
        center_title=True,
        bgcolor="AMBER",
        color="white"
    )

    # Estilo de encabezados
    encabezado = [
        ft.DataColumn(ft.Text("Cultivo", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
        ft.DataColumn(ft.Text("Parte", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
        ft.DataColumn(ft.Text("Cantidad", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
        ft.DataColumn(ft.Text("Área", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
        ft.DataColumn(ft.Text("Energía", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
        ft.DataColumn(ft.Text("Municipio", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
        ft.DataColumn(ft.Text("Latitud", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
        ft.DataColumn(ft.Text("Longitud", style=ft.TextStyle(size=14, weight="bold", color=ft.Colors.CYAN))),
    ]

    # Contenedor con estilo
    tabla_container = ft.Container(
        width=1300,
        height=400,
        bgcolor=ft.Colors.GREY_100,
        border_radius=10,
        padding=10,
        shadow=ft.BoxShadow(
            blur_radius=6,
            color=ft.Colors.GREY_400,
            offset=ft.Offset(2, 2),
            spread_radius=1
        ),
        animate_opacity=300,
        animate_scale=ft.Animation(400, "easeInOut"),
        opacity=0,
        scale=0.95
    )


    def cargar_datos():
        filas = []
        datos = at.Bioenergia.all()
        alternar_color = True

        for d in datos:
            bg_color = ft.Colors.WHITE if alternar_color else ft.Colors.GREY_200
            alternar_color = not alternar_color

            fila = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(d.cultivo), style=ft.TextStyle(size=13))),
                    ft.DataCell(ft.Text(str(d.parte), style=ft.TextStyle(size=13))),
                    ft.DataCell(ft.Text(str(d.cantidad), style=ft.TextStyle(size=13))),
                    ft.DataCell(ft.Text(str(d.area), style=ft.TextStyle(size=13))),
                    ft.DataCell(ft.Text(str(d.energia), style=ft.TextStyle(size=13))),
                    ft.DataCell(ft.Text(str(d.municipio), style=ft.TextStyle(size=13))),
                    ft.DataCell(ft.Text(str(d.latitud), style=ft.TextStyle(size=13))),
                    ft.DataCell(ft.Text(str(d.longitud), style=ft.TextStyle(size=13))),
                ],
                color=bg_color
            )
            filas.append(fila)

        tabla_container.content = ft.DataTable(
            columns=encabezado,
            rows=filas,
            divider_thickness=1,
            show_bottom_border=True,
            heading_row_color=ft.Colors.GREY_300,
            heading_row_height=48,
            data_row_min_height=44
        )

        tabla_container.opacity = 1
        tabla_container.scale = 1
        page.update()

        # Botón estilizado para el menú 
    def crear_boton(texto, icono, accion):
        return ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(icono, size=24, color=ft.Colors.WHITE),
                    ft.Text(texto, size=18, weight="bold", color=ft.Colors.WHITE)
                ],
                alignment="center",
                spacing=12
            ),
            on_click=accion,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=14),
                padding=ft.Padding(16, 12, 16, 12),
                bgcolor=ft.Colors.AMBER_300,
                overlay_color=ft.Colors.AMBER_100,
                elevation=4
            ),
            width=400 
    )

    btn_menu = crear_boton(
        "Menú principal",
        "MENU_OPEN",
        menu
    )

    columna_botones = ft.Column(
        controls=[
            btn_menu
        ],
        alignment="center",
        horizontal_alignment="center",
        spacing=20
    )


    # Agregar a la página
    page.add(
        ft.Column(
            controls=[
                columna_botones,
                tabla_container
                ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START
        )
    )

    # Cargar con animación
    cargar_datos()

if __name__ == "__main__":
    ft.app(target=main)
