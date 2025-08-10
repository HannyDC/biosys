import flet as ft
import airtable as at
import principal as pri
import main as ma

def main(page: ft.Page):

    def cuenta(e):
        page.clean()
        ma.main(page)

    def guardar_usuario(e: ft.ControlEvent):
        clave = txt_clave.value
        contra = txt_contra.value
        contra2 = txt_contra2.value
        nombre = txt_nombre.value

        #Validar campos
        if clave == "":
            snackbar = ft.SnackBar(ft.Text("Introduce tu clave de usuario"), bgcolor= "purple", show_close_icon=True)
            page.open(snackbar)
            return
        if contra == "":
            snackbar = ft.SnackBar(ft.Text("Contraseña incorrecta"), bgcolor= "red", show_close_icon=True)
            page.open(snackbar)
            return
        if nombre == "":
            snackbar = ft.SnackBar(ft.Text("Introduce su Nombre completo"), bgcolor= "red", show_close_icon=True)
            page.open(snackbar)
            return 
        
        #Confirmar contraseña
        if contra != contra2:
            snackbar = ft.SnackBar(ft.Text("Contraseña incorrecta"), bgcolor= "red", show_close_icon=True)
            page.open(snackbar)
            return

        #Guardar el usuario en la nube
        nuevo = at.usuario(
            clave = clave,
            contra =  contra,
            nombre = nombre,
            admin=chk_admin.value
        )

        try:
            nuevo.save()
            snackbar = ft.SnackBar(ft.Text("Usuario registrado"), bgcolor= "purple", show_close_icon= True)
            page.open(snackbar)
        except Exception as error:
            snackbar = ft.SnackBar(ft.Text(error), bgcolor= "red", show_close_icon= True)
            page.open(snackbar)



    def limpiar_campos():
        txt_clave.value = ""
        txt_contra.value = ""
        txt_contra2.value = ""
        txt_nombre.value = ""
        chk_admin.value = False
        page.update()

    # Página
    page.title = "Registro de Usuario"
    page.theme_mode = "light"
    page.window_width = 500
    page.window_height = 650
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.appbar = ft.AppBar(
        title=ft.Text("Alta de Usuario", size=20, weight="bold"),
        center_title=True,
        leading=ft.Icon("person_add"),
        bgcolor="purple",
        color="white"
    )

    # Formulario
    txt_clave = ft.TextField(label="Clave del usuario", width=400)
    txt_contra = ft.TextField(label="Contraseña", password=True, width=400, can_reveal_password=True)
    txt_contra2 = ft.TextField(label="Confirmar contraseña", password=True, width=400, can_reveal_password=True)
    txt_nombre = ft.TextField(label="Nombre completo", width=400)
    chk_admin = ft.Checkbox(label="¿Es administrador?", value=False)

    sesion = ft.TextButton(
        text="¿Ya tienes una cuenta? ¡Inicia sesión!",
        on_click=cuenta,
        style=ft.ButtonStyle(
        text_style=ft.TextStyle(
            size=16,  # tamaño del texto
            decoration=ft.TextDecoration.UNDERLINE,
            color="blue"
        )
    )
    )

    btn_guardar = ft.FilledButton(
        text="Guardar",
        icon="save",
        on_click=guardar_usuario,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10), 
            padding=15),
        bgcolor="purple"
    )

    btn_cancelar = ft.OutlinedButton(
        text="Cancelar",
        icon="cancel",
        on_click=lambda e: limpiar_campos(),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10), 
            padding=15),
    )

    fila_botones_principales = ft.Row(
        controls=[btn_guardar, btn_cancelar],
        alignment="center",
        spacing=20
    )



    columna_botones = ft.Column(
        controls=[
            fila_botones_principales,
        ],
        alignment="center",
        spacing=20
    )


    card = ft.Container(
        content=ft.Column(
            [
                txt_clave,
                txt_contra,
                txt_contra2,
                txt_nombre,
                chk_admin,
                columna_botones,
                sesion
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

    page.add(card)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)