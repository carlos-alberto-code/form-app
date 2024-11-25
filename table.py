import flet as ft


class Table(ft.DataTable):
    def __init__(self):
        super().__init__(
            columns = [
                ft.DataColumn(ft.Text("ID")),
                ft.DataColumn(ft.Text("Nombre")),
                ft.DataColumn(ft.Text("Edad")),
                ft.DataColumn(ft.Text('Telefono')),
            ],
        )
        self.rows = []

    def insert_entity(self, nombre: str, edad: str, telefono: str):
        self.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("1")),
                    ft.DataCell(ft.Text(nombre)),
                    ft.DataCell(ft.Text(edad)),
                    ft.DataCell(ft.Text(telefono)),
                ]
            )
        )

    def clear_table(self):
        self.rows = []

