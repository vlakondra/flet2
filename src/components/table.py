import flet as ft
import components as comp

users = comp.db.get_users()

txt = ft.Text(" ")

def ff():
    print('from ff')
    return comp.db.get_users()

ff()

def row_selected(e, i):
    print("row selected", i, e.data, e.control)

dt = ft.DataTable(
    columns=[
        ft.DataColumn(ft.Text("Имя")),
        ft.DataColumn(ft.Text("Отчество")),
        ft.DataColumn(ft.Text("Фамилия")),
    ],
    rows=[
        ft.DataRow(
            on_select_changed=lambda e, i=item: row_selected(e, i),
            selected=False,
            cells=[
                ft.DataCell(ft.Text(item[1])),
                ft.DataCell(ft.Text(item[2])),
                ft.DataCell(ft.Text(item[3]), show_edit_icon=True),
            ],
        )
        for item in ff() #users
    ],
)

cnt= ft.Container(content=dt, alignment= ft.alignment.top_center,)

