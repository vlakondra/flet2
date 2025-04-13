import flet as ft
import components as comp
from components.containers import containers, current_index

def switch_container(e):
        global current_index
        current_index = (current_index + 1) % len(containers)  # Увеличиваем индекс и обнуляем его при достижении конца списка
        print(e.page.controls)
        e.page.controls[0] = containers[current_index]  # Обновляем отображаемый контейнер
        e.page.update()  # Обновляем страницу

def main(page: ft.Page):
    comp.pageSettings(page)

    # Кнопка для переключения контейнеров
    switch_button = ft.ElevatedButton("Переключить контейнер", on_click=switch_container)
   
    page.add(containers[current_index], switch_button)

ft.app(main)
