import flet as ft
import alta_usuario as al
import consulta_usuario as cu
import alta_bioenergia as alb
import consultar_bionergias as cbio

def main(page: ft.Page):

    page.floating_action_button = None
    page.floating_action_button_location = None
    page.update()
    
    def mostrar_registro(e):
        page.clean()
        al.main(page)

    def consultar_usuario(e):
        page.clean()
        cu.main(page)

    def agregar_bio(e):
        page.clean()
        alb.main(page)

    def consultar_bio(e):
        page.clean()
        cbio.main(page)

    # Configuración general
    page.title = "Menú Principal"
    page.theme_mode = "light"
    page.window_width = 500
    page.window_height = 650
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 20

    page.appbar = ft.AppBar(
        title=ft.Text("Sistema de Gestión de Bioenergía", style=ft.TextStyle(size=20, weight="bold")),
        leading=ft.Icon(name="energy_savings_leaf"),
        center_title=True,
        bgcolor="pink",
        color="white"
    )

    # Título decorativo
    titulo = ft.Text(
        "Menú Principal",
        size=24,
        weight="bold",
        color=ft.Colors.PINK_400,
    )

    # Botón estilizado
    def crear_boton(texto, icono, accion):
        return ft.ElevatedButton(
            content=ft.Row(
                [
                    ft.Icon(icono, size=26),
                    ft.Text(texto, size=18)
                ],
                alignment="center",
                spacing=10
            ),
            on_click=accion,
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=12),
                padding=20,
                bgcolor=ft.Colors.PINK_100,
                overlay_color=ft.Colors.PINK_300
            ),
            expand=True
        )

    # Botones
    btn_registro = crear_boton("Registro de Usuario", "person_add", mostrar_registro)
    btn_consultas = crear_boton("Consulta de Usuario", "search", consultar_usuario)
    btn_agregar = crear_boton("Registro de Bioenergía", "eco", agregar_bio)
    btn_consultas_bio = crear_boton("Consulta de Bioenergía", "cloud_done", consultar_bio)

    # Tarjeta visual central
    card = ft.Container(
        content=ft.Column(
            [
                titulo,
                btn_registro,
                btn_consultas,
                btn_agregar,
                btn_consultas_bio,
            ],
            alignment="center",
            horizontal_alignment="center",
            spacing=20
        ),
        width=400,
        padding=30,
        border_radius=15,
        bgcolor=ft.Colors.GREY_100,
        shadow=ft.BoxShadow(
            blur_radius=8,
            color=ft.Colors.GREY_400,
            offset=ft.Offset(2, 4),
            spread_radius=1,
        )
    )

    # Agregar todo
    page.add(card)
    page.update()

# Iniciar app
if __name__ == "__main__":
    ft.app(target=main)
