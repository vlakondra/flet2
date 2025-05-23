import flet as ft
import pandas as pd
from datetime import datetime

def main(page: ft.Page):
    page.title = "DataFrame ListView"
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # Создаем пример DataFrame с разными типами данных
    data = {
        "ID": [1, 2, 3, 4, 5],
        "Name": ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"],
        "Description": [
            "Очень длинное описание товара, которое может занимать несколько строк и даже больше...",
            "Короткое описание",
            "Еще одно длинное описание с деталями и спецификациями продукта",
            "Среднее описание, которое содержит важные характеристики",
            "Минималистичное описание"
        ],
        "Date": [
            datetime(2023, 1, 1),
            datetime(2023, 2, 15),
            datetime(2023, 3, 30),
            datetime(2023, 4, 10),
            datetime(2023, 5, 20)
        ],
        "Price": [99.99, 149.50, 299.00, 199.95, 399.00]
    }
    
    df = pd.DataFrame(data)

    # Функция для создания строки таблицы
    def create_row(index, row, bg_color):
        return ft.Container(
            ft.Row(
                controls=[
                    ft.Container(
                        ft.Text(str(row[col]), 
                                overflow=ft.TextOverflow.ELLIPSIS,
                                no_wrap=True),
                        width=100,
                        padding=5,
                        expand=True
                    ) for col in df.columns
                ],
                vertical_alignment=ft.CrossAxisAlignment.START
            ),
            bgcolor=bg_color,
            padding=ft.padding.symmetric(vertical=5),
            border=ft.border.only(
                bottom=ft.border.BorderSide(1, ft.colors.GREY_300)
            )
        )

    # Создаем заголовок таблицы
    header = ft.Container(
        ft.Row(
            controls=[
                ft.Container(
                    ft.Text(col, 
                            weight=ft.FontWeight.BOLD,
                            color=ft.colors.BLUE_GREY_700),
                    width=100,
                    padding=5,
                    expand=True
                ) for col in df.columns
            ]
        ),
        bgcolor=ft.colors.BLUE_GREY_50,
        padding=ft.padding.symmetric(vertical=10),
        border=ft.border.all(1, ft.colors.GREY_300)
    )

    # Создаем список элементов данных
    rows = []
    for index, row in df.iterrows():
        rows.append(
            create_row(
                index,
                row,
                bg_color=ft.colors.WHITE if index % 2 == 0 else ft.colors.GREY_50
            )
        )

    # Собираем интерфейс
    page.add(
        ft.Column(
            controls=[
                ft.Text("Список товаров", 
                       size=20,
                       weight=ft.FontWeight.BOLD),
                header,
                ft.Container(
                    ft.ListView(
                        controls=rows,
                        expand=True,
                        spacing=0,
                        padding=0
                    ),
                    height=400,
                    border=ft.border.all(1, ft.colors.GREY_300))
            ],
            spacing=10
        )
    )

ft.app(target=main)