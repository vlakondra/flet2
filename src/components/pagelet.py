import flet as ft
from importlib import reload

from db.dbwork import dbWork
from components.table import cnt, dt, txt, ff
import components as comp


def show1(e):
    if e.data == "1":
        pagelet.content = t1
    elif e.data == "0":
        pagelet.content = cnt

name = ft.TextField()
lastName = ft.TextField()
fam = ft.TextField()

def addData(e):
    print(name.current.value)
    comp.db.add_user(name.current.value, lastName.current.value, fam.current.value)

    e.page.update()
    # pagelet.content = cnt
    # cnt.update()
    ff()


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
                controls=[
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
            content=ft.Text("This is Tab 2"),
        ),
        ft.Tab(
            text="Tab 3",
            icon=ft.Icons.SETTINGS,
            content=ft.Text("This is Tab 3"),
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
