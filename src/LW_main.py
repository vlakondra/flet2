import flet as ft
import pandas as pd

def dataframe_to_listview(df: pd.DataFrame):
    controls = []
    
    
    # Формируем заголовок таблицы (имена колонок) как отдельный ListTile
    header = ft.ListTile(
        title=ft.Row(
            [ft.Container(ft.Text(str(col), weight=ft.FontWeight.BOLD), width=200, padding=5) for col in df.columns],
            scroll=ft.ScrollMode.HIDDEN
        ),
        bgcolor=ft.colors.BLUE_GREY_100,
        dense=True,
        content_padding=10
    )
    controls.append(header)

    # Формируем строки данных
    for _, row in df.iterrows():
        row_controls = []
        for item in row:
            # Преобразуем значение в строку, чтобы избежать проблем с разными типами, и ограничиваем длиной с переносом
            cell_text = str(item)
            # Используем Container для фиксированной ширины с возможностью переноса текста
            cell = ft.Container(
                ft.Text(cell_text, overflow=ft.TextOverflow.VISIBLE, no_wrap=False),
                width=200,
                padding=5,
            )
            row_controls.append(cell)

        list_tile = ft.ListTile(
            title=ft.Row(row_controls, scroll=ft.ScrollMode.AUTO),
            content_padding=10,
            dense=True
        )
        controls.append(list_tile)

    return ft.ListView(
        controls=controls,
        expand=True,
        spacing=2,
        padding=10,
    )

def main(page: ft.Page):
    page.title = "Pandas DataFrame в ListView"
    page.window_width = 900
    page.window_height = 600

    #Пример построения DataFrame из SQL-запроса
    # https://colab.research.google.com/drive/11khiDO5Rn89NY2l8oKaGJ6NdI75QfutQ#scrollTo=m_qUXf8qQC41

    # Пример DataFrame с разными типами данных и длинными строками
    df = pd.DataFrame({
        "ID": [1, 2, 3],
        "Name": ["Alice", "Bob with a very long name that should wrap", "Charlie"],
        "Age": [25, 30, 35],
        "Description": [
            "Short description",
            "This is a very very very long description text that should wrap nicely inside the list view container to demonstrate text wrapping functionality.",
            "Another short one"
        ],
        "Active": [True, False, True]
    })

    list_view = dataframe_to_listview(df)

    page.add(list_view)

ft.app(target=main)
