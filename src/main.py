import flet as ft
from flet.core.box import List
import components as comp
from components.containers import containers, current_index

from components.catsDialog import show_dialog
from restapi.cats import getBreeds

from components.pagelet import pagelet


# https://thecatapi.com/


def ff():
    brs = getBreeds()
    print(brs)
    return brs

def onerr(e):
    print('onerr',e)

# import logging
# logging.basicConfig(level=logging.DEBUG)


def main(page: ft.Page):
    comp.pageSettings(page)
    # получим массив пород
    # page.run_thread(ff)
    page.auto_scroll = True

    # создадим список для отображения пород
    lv = ft.ListView(expand=False, spacing=10, width=202, height=400, horizontal=False)

    # breeds = await getBreeds()
    breeds = getBreeds() #Данные по породам
  
    # Создадим форму отображения данных:
    # Контейнер-колонка-изображение-подпись
    for breed in breeds:
        img = ft.Image(
            src=f"https://cdn2.thecatapi.com/images/{breed['reference_image_id']}.jpg",
            width=200,
            # height=100,
            fit=ft.ImageFit.CONTAIN,
            error_content=ft.Text("", width=100),
        )

        # print(img.src)

        nm = ft.TextButton(
            breed["name"],
            on_click=lambda e, b_id=breed["id"], b_name=breed["name"]: show_dialog(
                e, b_id, b_name
            ),
            width=195,
        )

        col = ft.Column(
            spacing=0, alignment=ft.MainAxisAlignment.START, controls=[img, nm]
        )

        cnt = ft.Container(
            content=col,
            expand=False,
            padding=10,
            border=ft.border.all(1, ft.Colors.PINK_600),
        )
        
        lv.controls.append(cnt)

    page.on_error=onerr    

    page.add(lv)


ft.app(main)
