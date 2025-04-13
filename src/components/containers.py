import flet as ft
from components import fam


def onclick(e):
    fam.current.value = fam.current.value + "!"
    fam.update()


container1 = ft.Container(
    bgcolor=ft.colors.RED,
    width=200,
    height=200,
    expand=False,
    alignment= ft.alignment.top_center,
    content=ft.ElevatedButton("Кнопка", on_click=onclick),
)

container2 = ft.Container(bgcolor=ft.colors.GREEN, width=200, height=200)

container3 = ft.Container(
    bgcolor=ft.colors.BLUE,
    width=200,
    height=200,
    content=ft.TextField(
        ref=fam,
        label="Фамилия",
        autofocus=True,
    ),
)


# Список контейнеров
containers = [container1, container2, container3]
current_index = 0  # Индекс текущего контейнера
