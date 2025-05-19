import flet as ft

def main(page: ft.Page):
    # Настройка страницы
    page.title = "Обновляемая таблица"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
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
        ###???
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
        "Добавить строку", icon=ft.icons.ADD, on_click=add_row
    )

    select_file = ft.ElevatedButton(
        "Выбрать файл БД",
        icon=ft.icons.FILE_OPEN,
        on_click=lambda _: file_picker.pick_files(allow_multiple=False),
    )

    def on_dialog_result(e: ft.FilePickerResultEvent):
        print("Selected files:", e.files)
        print("Selected file or directory:", e.path)

        var.value=str(var.value)+'1'
        print(var.value)
        page.update()

    #Добавляем диалог выбора файла
    #https://flet.dev/docs/controls/filepicker
    file_picker = ft.FilePicker(on_result=on_dialog_result)
    page.overlay.append(file_picker)

    var =ft.Text(str(1))
    page.overlay.append(var)

    page.update()

    # Добавляем элементы на страницу
    page.add(
        ft.Column(
            [
                var,
                select_file,
                add_button,
                ft.Container(
                    table,
                    border=ft.border.all(1, ft.colors.OUTLINE),
                    padding=10,
                    border_radius=5,
                ),
            ],
            spacing=20,
        )
    )
    page.update()


ft.app(target=main)
