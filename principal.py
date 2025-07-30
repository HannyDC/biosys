import flet as ft 

def main (page: ft.Page):
    def mostrar_registro(e:ft.ControlEvent):
        page.clean()
    #configuracion de la pagina
    page.title="Menu principal"
    page.theme_mode="light"
    page.window.width = 500
    page.window.height = 650
    page.appbar=ft.AppBar(
        title=ft.Text("Sistema de gestion de bioenergias"),
        leading=ft.Icon("energy_savings_leaf"),
        color="white",
        bgcolor="pink"
    )
    #Componentes de la pagina 
    btn_registro=ft.ElevatedButton("Registro")
    btn_consultas=ft.ElevatedButton("Consulta")
    #Añadir a la pagina 
    page.add(btn_registro,btn_consultas)
    page.update()

#Inicio de la aplicación 
if __name__=="__main__":
    ft.app(target=main)
