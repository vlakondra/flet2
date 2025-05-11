import flet as ft
from flet import Colors

from peewee import *;
from playhouse.reflection import Introspector

odb = SqliteDatabase('storage/data/chinook.db')
introspector = Introspector.from_database(odb)
models = introspector.generate_models()

print('odb',models,odb)









def pageSettings(page):
    '''Настройка главной страницы'''
    page.title = "Пример"
    page.vertical_alignment=ft.MainAxisAlignment.START,
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    page.padding = 15
    page.bgcolor=Colors.GREY_100
    page.theme_mode =ft.ThemeMode.SYSTEM
    page.window.prevent_close = True
    page.window.center()
