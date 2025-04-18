import flet as ft
from flet import Colors

from db.dbwork import dbWork
db = dbWork('users.db')


def pageSettings(page):
    '''Настройка главной страницы'''
    page.title = "Пример"
    page.vertical_alignment=ft.MainAxisAlignment.START
    page.padding = 15
    page.bgcolor=Colors.GREY_100
    page.theme_mode =ft.ThemeMode.SYSTEM
    page.window.prevent_close = True
    page.window.center()

fam = ft.Ref[ft.TextField]()    