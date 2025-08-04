import flet as ft 
import principal as pr
from airtable import usuario as Usuario
from pyairtable.formulas import match 

Usuario.api_key = "patddj75juQQctN64.640cb9e46f034de99df77e9f25843de1da99b34889974c2ef6bfe780ef604079"
Usuario.base_id = "app0792rIxoA7dOn3"
Usuario.table_name = "usuario"

# Funcion principal
def main (page: ft.Page):

    def ingresar (e: ft.ControlEvent):
        usuario_valor = txt_usuario.value.strip()
        password_valor = txt_pass.value.strip()
        try: 
            formula = match ({"clave": usuario_valor, "contra": password_valor}) 
            registro = Usuario.first(formula=formula)
            if registro:
                print("Funciona!")
                # desplegar pricipal.py
                page.clean()
                pr.main(page)
            else: 
                print(f"Usuario '{usuario_valor}' no encontrado.")
                # mostrar la snackbar
        except Exception as e:
            print (f"Error de Airtable: {e}")
            #mostrar la snackbar

    #configuracion de la pagina 
    page.theme_mode = "light"
    page.horizontal_alignment = "center"
    page.title = "Inicio de sesion"
    page.window.width = 500
    page.window.height = 650

    #Componentes de la pagina
    logo = ft.Icon("Person", size=100, color="Pink")
    txt_bienvenido = ft.Text("Bienvenido", size=30)
    txt_usuario= ft.TextField(label="Username/Correo", width=300)
    espacio1 = ft.Container(height=10)  # Espacio entre campos
    txt_pass= ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300)
    espacio2 = ft.Container(height=10)  # Espacio entre campos
    btn_login = ft.FilledButton (
        "Iniciar sesion", 
        icon=ft.Icons.LOGIN, 
        width=250,
        color="White",
        bgcolor= "pink", 
        on_click= ingresar
        )

    page.add(logo, txt_bienvenido, txt_usuario, txt_pass, btn_login)

    #Actualizar la pagina
    page.update()

if __name__=="__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)