import flet as ft
import components as comp
from components.containers import containers, current_index

from components.catsDialog import show_dialog
from restapi.cats import getBreeds

from components.pagelet import pagelet


def switch_container(e):
    global current_index
    current_index = (current_index + 1) % len(
        containers
    )  # Увеличиваем индекс и обнуляем его при достижении конца списка
    print(e.page.controls)
    e.page.controls[0] = containers[current_index]  # Обновляем отображаемый контейнер
    e.page.update()  # Обновляем страницу

# https://thecatapi.com/

def main(page: ft.Page):
    comp.pageSettings(page)
    #получим массив пород
    breeds = getBreeds()

    # создадим список для отображения пород
    lv = ft.ListView(expand=False, spacing=10, width=202,height=400, horizontal=False)

    #Создадим форму отображения данных:
    #Контейнер-колонка-изображение-подпись
    for breed in breeds:
        img = ft.Image(
            src=f"https://cdn2.thecatapi.com/images/{breed['reference_image_id']}.jpg",
            width=200,
            height=100,
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("", width=100),
            
        )

        nm = ft.TextButton(breed['name'],
          on_click = lambda e, b_id = breed['id'], b_name=breed['name']: show_dialog(e, b_id, b_name),
          width = 195,)
        
        col = ft.Column(spacing=0,
            alignment=ft.MainAxisAlignment.START,
            controls=[img,nm])

        cnt =ft.Container(
            content=col,
            expand=False,
            padding=10,
            border=ft.border.all(1, ft.Colors.PINK_600))    

        lv.controls.append(cnt)

    page.add(lv)

ft.app(main)
