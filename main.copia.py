import flet as ft  
#import modelo as md #solo es local 
from airtable import usuario as Usuario 
import principal as pr
from pyairtable.formulas import match

#Funcion principal 

Usuario.api_key="patddj75juQQctN64.640cb9e46f034de99df77e9f25843de1da99b34889974c2ef6bfe780ef604079"
Usuario.base_id="app0792rIxoA7dOn3"
Usuario.table_name="usuario"

def main (page: ft.Page):
    def ingresar (e: ft.ControlEvent):
        usuario_valor = txt_usuario.value.strip()
        password_valor = txt_contraseña.value.strip()
        try:
            formula = match ({"clave": usuario_valor, "contra": password_valor })
            registro = Usuario.first(formula=formula)
            if registro:
                print("¡Funciona!")
                page.clean()
                pr.main(page)  
            else:
                print(f"Usuario '{usuario_valor}' no encontrado.")
                
        except Exception as e:
            print(f"Error de Airtable: {e}")
            


    #configuración de la pagina 
    page.theme_mode="light"
    page.horizontal_alignment="center"
    page.title="Inicio de Sesión"
    page.window.width=600
    page.window.height=700

    #Componentes de la pagina
    logo=ft.Icon("person", size=150, color="green")
    txt_bienvenido=ft.Text("Bienvenid@",size=38,color="green")
    txt_usuario=ft.TextField(label="Username/correo",width=300)
    espacio1 = ft.Container(height=10)  # Espacio entre campos
    txt_contraseña=ft.TextField(label="Contraseña", password=True, can_reveal_password=True,width=300)
    espacio2 = ft.Container(height=10)  # Espacio entre campos
    btn_login=ft.FilledButton(text="Iniciar Sesion", icon=ft.Icons.LOGIN, width=250,bgcolor="green",on_click=ingresar)

    page.add(logo,txt_bienvenido,txt_usuario,espacio1,txt_contraseña,espacio2,btn_login)
    #Actualizar la pagina
    page.update()

#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)


