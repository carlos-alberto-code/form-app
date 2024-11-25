import flet as ft

class Form(ft.Container):
    def __init__(self, on_save=None, on_clear=None):
        super().__init__()
        self._title = "Formulario"
        self.width = 400
        self.height = 300
        self.padding = 10
        self.border = ft.border.all(1, 'black')
        self.border_radius = 10
        self.alignment = ft.alignment.center
        self._on_clear = on_clear
        self.content = ft.Column(
            controls=[
                ft.Text(
                    value="Registro de personas",
                    size=20,
                    weight=ft.FontWeight.W_400,
                ),
                ft.TextField(
                    label="Nombre",
                    width=300,
                    height=45,
                    border_radius=10,
                ),
                ft.TextField(
                    label="Edad",
                    width=300,
                    height=45,
                    border_radius=10,
                ),
                ft.TextField(
                    label="Telefono",
                    width=300,
                    height=45,
                    border_radius=10,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            text="Borrar",
                            on_click=self.on_clear
                        ),
                        ft.ElevatedButton(
                            text="Guardar",
                            on_click=on_save
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

        )

    @property
    def on_clear(self):
        return self._on_clear

    @on_clear.setter
    def on_clear(self, value):
        self._on_clear = value

    def get_data(self):
        return {
            "nombre": self.content.controls[1].value,
            "edad": self.content.controls[2].value,
            "telefono": self.content.controls[3].value,
        }
