import flet as ft
from flet import Colors

class MyButton(ft.ElevatedButton):
    """Кнопка для проверки"""

    def __init__(self, text, onclick):
        super().__init__()
        self.bgcolor = Colors.BLUE_300
        self.color = ft.Colors.GREEN_800
        self.text = text
        self.on_click = onclick