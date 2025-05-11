import flet as ft

from db.dbwork import dbWork
from components.table import  txt, func,getDataTable
import components as comp

var =10
def show1(e):
    global var
    if e.data == "1":
        pagelet.content = t1
    elif e.data == "0":
        var=var+1
        print('show1??',var, e.data)
        pagelet.content = getDataTable()

    pagelet.update()    



name = ft.Ref[ft.TextField]()
lastName = ft.Ref[ft.TextField]()
fam = ft.Ref[ft.TextField]()


def addData(e):
    print(name.current.value)
    comp.db.add_user(name.current.value, lastName.current.value, fam.current.value)

    e.page.update()



t1 = ft.Tabs(
    selected_index=0,
    animation_duration=300,
    width=960,
    tabs=[
        ft.Tab(
            text="Tab 1",
            content=ft.Column(
                spacing=10,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Text(""),
                    ft.TextField(
                        ref=name, label="Имя", multiline=True, max_lines=3, width=150
                    ),
                    ft.TextField(ref=lastName, label="Отчество", width=150),
                    ft.TextField(ref=fam, label="Фамилия", width=150),
                    ft.Button("Сохранить", on_click=addData),
                ],
            ),
        ),
        ft.Tab(
            tab_content=ft.Icon(ft.Icons.SEARCH),
            content=ft.Text("Закладка Tab 2"),
        ),
        ft.Tab(
            text="Tab 3",
            icon=ft.Icons.SETTINGS,
            content=ft.Text("Закладка Tab 3"),
        ),
    ],
    expand=1,
)


pagelet = ft.Pagelet(
    appbar=ft.AppBar(
        title=ft.Text("Простой пример Pagelet"),
        bgcolor=ft.Colors.AMBER_ACCENT,
    ),
    content=txt,
    bgcolor=ft.Colors.AMBER_100,
    drawer=ft.NavigationDrawer(
        on_change=show1,
        controls=[
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ADD_TO_HOME_SCREEN_SHARP, label="Таблица"
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icons.ADD_COMMENT,
                label="Табулятор",
            ),
        ],
    ),
    height=700,
    expand=True,
)
