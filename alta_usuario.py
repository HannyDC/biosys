import flet as ft 
import airtable as at

def main(page: ft.Page):

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


    #Configuracion de la pagina 
    page.title = "Altas"
    page.theme_mode= "light"
    page.window.width = 500
    page.window.height = 650
    page.appbar = ft.AppBar(
        title=ft.Text("Nuevo usuario"),
        center_title=True,
        leading=ft.Icon("Person_add"),
        color=("white"),
        bgcolor=("pink")
    )

    #componentes 
    txt_clave = ft.TextField(label="Clave del usuario")
    txt_contra = ft.TextField(label="Contraseña", password=True)
    txt_contra2 = ft.TextField(label="Confirmar contraseña", password=True)
    txt_nombre = ft.TextField(label="Nombre completo")
    chk_admin = ft.Checkbox(label="¿Es administrador?")
    btn_guardar = ft.FilledButton(
        text="Guardar",
        icon= "SAVE",
        on_click= guardar_usuario,
        bgcolor=("purple")
    )
    btn_cancelar= ft.FilledButton(
        text="Cancelar",
        icon="cancel",
        bgcolor=("purple")
    )

    fila = ft.Row(controls=[btn_guardar,btn_cancelar])

    page.add(txt_clave, txt_contra, txt_contra2, txt_nombre, chk_admin, fila)
    page.update ()

if __name__=="__main__":
    ft.app(target=main)