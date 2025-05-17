import flet as ft

def main(page: ft.Page):
    # Настройка страницы
    page.title = "Обновляемая таблица"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.padding = 20

    # Создаем DataTable с колонками
    table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Название")),
            ft.DataColumn(ft.Text("Значение")),
        ],
    )

    # Счетчик для генерации новых строк
    counter = 1

    def add_row(e):
        nonlocal counter
        # Добавляем новую строку
        table.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(counter))),
                    ft.DataCell(ft.Text(f"Элемент {counter}")),
                    ft.DataCell(ft.Text(f"Значение {counter}")),
                ]
            )
        )
        counter += 1
        page.update()

    # Создаем кнопку добавления
    add_button = ft.ElevatedButton(
        "Добавить строку",
        icon=ft.icons.ADD,
        on_click=add_row
    )

    # Добавляем элементы на страницу
    page.add(
        ft.Column(
            [
                add_button,
                ft.Container(
                    table,
                    border=ft.border.all(1, ft.colors.OUTLINE),
                    padding=10,
                    border_radius=5,
                )
            ],
            spacing=20
        )
    )

ft.app(target=main)