import flet as ft
from form import Form
from table import Table

def main(page: ft.Page):
    page.title = "Formulario"
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_on_save(event: ft.ControlEvent):
        table.insert_entity(
            nombre=form.get_data()["nombre"],
            edad=form.get_data()["edad"],
            telefono=form.get_data()["telefono"],
        )
        table.update()

    def handle_on_clear(event: ft.ControlEvent):
        table.clear_table()
        table.update()

    form = Form(on_save=handle_on_save, on_clear=handle_on_clear)
    table = Table()

    page.add(
        ft.Row(
            [
                form,
                table,
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START,
        )
    )


ft.app(target=main)
