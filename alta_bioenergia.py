import flet as ft
import airtable as at
import principal as pri

def main(page: ft.Page):
    
    def guardar_bio(e: ft.ControlEvent):
        cultivo = txt_cultivo.value
        parte = txt_parte.value
        municipio = select_municipio.value if select_municipio.value else ""

        if cultivo == "":
            page.open(ft.SnackBar(ft.Text("Introduce el nombre del cultivo"), bgcolor="purple", show_close_icon=True))
            return
        if parte == "":
            page.open(ft.SnackBar(ft.Text("Introduce la parte del cultivo"), bgcolor="purple", show_close_icon=True))
            return

        try:
            cantidad = float(txt_cantidad.value)
            area = float(txt_area.value)
            energia = float(txt_energia.value)
        except ValueError:
            page.open(ft.SnackBar(ft.Text("Introduce valores numéricos válidos"), bgcolor="purple", show_close_icon=True))
            return

        if municipio == "":
            page.open(ft.SnackBar(ft.Text("Selecciona un municipio"), bgcolor="purple", show_close_icon=True))
            return

        try:
            latitud = float(txt_latitud.value)
            longitud = float(txt_longitud.value)
        except ValueError:
            page.open(ft.SnackBar(ft.Text("Introduce valores numéricos válidos"), bgcolor="purple", show_close_icon=True))
            return

        nueva_bio = at.Bioenergia(
            cultivo=cultivo,
            parte=parte,
            cantidad=cantidad,
            area=area,
            energia=energia,
            municipio=municipio,
            latitud=latitud,
            longitud=longitud
        )

        try:
            nueva_bio.save()
            page.open(ft.SnackBar(ft.Text("Cultivo registrado exitosamente"), bgcolor="purple", show_close_icon=True))
        except Exception as error:
            page.open(ft.SnackBar(ft.Text(str(error)), bgcolor="red", show_close_icon=True))

    def limpiar_campos():
        txt_cultivo.value = ""
        txt_parte.value = ""
        txt_cantidad.value = ""
        txt_area.value = ""
        txt_energia.value = ""
        select_municipio.value = ""
        txt_latitud.value = ""
        txt_longitud.value = ""
        page.update()

    # Configuración de la página
    page.title = "Registro de Bioenergía"
    page.theme_mode = "light"
    page.window_width = 500
    page.window_height = 700
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    page.appbar = ft.AppBar(
        title=ft.Text("Nueva Bioenergía", size=20, weight="bold"),
        center_title=True,
        leading=ft.Icon("eco"),
        bgcolor="lightgreen",
        color="white"
    )

    # Campos
    txt_cultivo = ft.TextField(label="Cultivo", width=400)
    txt_parte = ft.TextField(label="Parte del cultivo", width=400)
    txt_cantidad = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    txt_area = ft.TextField(label="Área", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    txt_energia = ft.TextField(label="Energía generada", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    select_municipio = ft.Dropdown(
        label="Municipio",
        width=400,
        options=[ft.dropdown.Option(m) for m in [
            "Balancán", "Cárdenas", "Centla", "Centro", "Comalcalco",
            "Cunduacán", "Emiliano Zapata", "Huimanguillo", "Jalapa",
            "Jalpa de Méndez", "Jonuta", "Macuspana", "Nacajuca",
            "Paraíso", "Tacotalpa", "Teapa", "Tenosique"
        ]]
    )
    txt_latitud = ft.TextField(label="Latitud", keyboard_type=ft.KeyboardType.NUMBER, width=400)
    txt_longitud = ft.TextField(label="Longitud", keyboard_type=ft.KeyboardType.NUMBER, width=400)

    # Botones
    btn_guardar = ft.FilledButton(
        text="Guardar",
        icon="save",
        on_click=guardar_bio,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=20),
        bgcolor="green"
    )
    btn_cancelar = ft.FilledButton(
        text="Cancelar",
        icon="cancel",
        on_click=lambda e: limpiar_campos(),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10), padding=20),
        bgcolor="grey"
    )

    fila_botones = ft.Row(
        controls=[btn_guardar, btn_cancelar],
        alignment="center",
        spacing=20
    )

    # Botón flotante solo para esta pantalla
    def volver(e):
        page.floating_action_button = None
        page.floating_action_button_location = None
        page.update()
        page.clean()
        pri.main(page)


    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ARROW_BACK,
        focus_color="black",
        on_click=volver
    )
    page.floating_action_button_location = ft.FloatingActionButtonLocation.END_FLOAT

   
    formulario = ft.Column(
        controls=[
            txt_cultivo,
            txt_parte,
            txt_cantidad,
            txt_area,
            txt_energia,
            select_municipio,
            txt_latitud,
            txt_longitud,
            fila_botones
        ],
        spacing=15,
        alignment="center",
        horizontal_alignment="center"
    )

    page.add(formulario)

if __name__ == "__main__":
    ft.app(target=main)
