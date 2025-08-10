import flet as ft
import principal as pr
import modelo as md
import alta_usuario as al

def main(page: ft.Page):

    def registrarse(e):
        page.clean()
        al.main(page)

    def ingresar(e: ft.ControlEvent):
                #validar campos
        usuario = txt_usuario.value
        Contraseña = txt_pass.value
        snackbar = ft.SnackBar(ft.Text("Introduce tu usuario"), bgcolor="blue", show_close_icon=True)
        if usuario == "":
            snackbar.content = (ft.Text("Introduce tu usuario"))
            page.open(snackbar)
            return
        elif Contraseña == "":
            snackbar.content = (ft.Text("Introduce tu contraseña"))
            page.open(snackbar)
            return

        #verificar usuario en la base de datos
        x= md.Usuario.select().where(
            md.Usuario.clave == usuario,
            md.Usuario.contra == Contraseña
        ) 
        if len(x) == 0:
            snackbar.content = ft.Text("Credenciales incorrectas")
            page.open(snackbar)
        else:
            page.clean()
            pr.main(page)

    # Configuración de la página
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.title = "Inicio de sesión"
    page.window_width = 500
    page.window_height = 650
    page.padding = 20

    page.appbar = ft.AppBar(
    title=ft.Text("Inicio de Sesión", size=20, weight="bold"),
    center_title=True,
    bgcolor=ft.Colors.PINK_300,
    color="white",
    )

    # Logo + título
    logo = ft.Icon(name="person", size=80, color=ft.Colors.PINK)
    titulo = ft.Text("Bienvenido", size=26, weight="bold", color=ft.Colors.PINK_600)

    # Campos de texto
    txt_usuario = ft.TextField(label="Usuario o Correo", width=300)
    txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)

    incio_sesion = ft.TextButton(
        text="¿No tienes una cuenta? ¡Registrate aqui!",
        on_click=registrarse,
        style=ft.ButtonStyle(
        text_style=ft.TextStyle(
            size=16,  # tamaño del texto
            decoration=ft.TextDecoration.UNDERLINE,
            color="blue"
        )
    )
    )

    # Botón de inicio
    btn_login = ft.ElevatedButton(
        content=ft.Row(
            [ft.Icon(ft.Icons.LOGIN, size=22), ft.Text("Iniciar sesión", size=16)],
            alignment="center",
            spacing=10
        ),
        width=260,
        height=50,
        bgcolor=ft.Colors.PINK_300,
        color="white",
        on_click=ingresar,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.Colors.PINK_100
        )
    )

    # Tarjeta central
    tarjeta = ft.Container(
        content=ft.Column(
            [
                logo,
                titulo,
                txt_usuario,
                txt_pass,
                btn_login,
                incio_sesion
            ],
            spacing=20,
            alignment="center",
            horizontal_alignment="center"
        ),
        width=400,
        padding=30,
        border_radius=15,
        bgcolor=ft.Colors.GREY_100,
        shadow=ft.BoxShadow(
            blur_radius=8,
            color=ft.Colors.GREY_400,
            offset=ft.Offset(2, 4),
            spread_radius=1
        )
    )

    page.add(tarjeta)
    page.update()

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
