import flet as ft
import airtable as at
import principal as pri

def main(page: ft.Page):

    def menu(e):
        page.clean()
        pri.main(page)

    # Configuración de la página
    page.title = "Consulta"
    page.theme_mode = "light"
    page.window_width = 600
    page.window_height = 700
    page.horizontal_alignment = "center"
    page.padding = 20

    
    page.appbar = ft.AppBar(
        title=ft.Text("Consulta de Usuario en la Nube", style=ft.TextStyle(size=22, weight="bold")),
        leading=ft.Icon(name="cloud", size=30),
        center_title=True,
        bgcolor="TEAL",
        color="white"
    )

    # Encabezado con estilo personalizado
    encabezado = [
        ft.DataColumn(ft.Text("Clave", style=ft.TextStyle(size=16, weight="bold", color=ft.Colors.BLUE))),
        ft.DataColumn(ft.Text("Contraseña", style=ft.TextStyle(size=16, weight="bold", color=ft.Colors.BLUE))),
        ft.DataColumn(ft.Text("Nombre Completo", style=ft.TextStyle(size=16, weight="bold", color=ft.Colors.BLUE))),
        ft.DataColumn(ft.Text("Administrador", style=ft.TextStyle(size=16, weight="bold", color=ft.Colors.BLUE)))
    ]

    # Contenedor animado
    tabla_container = ft.Container(
        width=1400,
        height=500,
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
                bgcolor=ft.Colors.TEAL_200,
                overlay_color=ft.Colors.TEAL_500,
                elevation=4
            ),
            width=400  
    )

    btn_menu = crear_boton(
        "Menú principal",
        "MENU_OPEN",
        menu
    )

    def cargar_datos():
        filas = []
        datos = at.usuario.all()
        alternar_color = True

        for d in datos:
            bg_color = ft.Colors.WHITE if alternar_color else ft.Colors.GREY_200
            alternar_color = not alternar_color

            fila = ft.DataRow(
                [
                    ft.DataCell(ft.Text(d.clave, style=ft.TextStyle(size=14))),
                    ft.DataCell(ft.Text("", style=ft.TextStyle(size=14))),
                    ft.DataCell(ft.Text(d.nombre, style=ft.TextStyle(size=14))),
                    ft.DataCell(ft.Text(d.admin, style=ft.TextStyle(size=14))),
                ],
                color=bg_color,
                selected=False,
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

    columna_botones = ft.Column(
        controls=[
            btn_menu
        ],
        alignment="center",
        spacing=20
    )

    # Agregar al page
    page.add(
        ft.Column(
            [
                columna_botones,
                tabla_container
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.START
        )
    )

    cargar_datos()


if __name__ == "__main__":
    ft.app(target=main)
