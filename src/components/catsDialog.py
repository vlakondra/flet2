import flet as ft
from restapi.cats import getCatsByBreed

def show_dialog(e,br_id, br_name):
    '''Функция для отображения диалогового окна 
    с изображениями кошек определенной породы.
    br_id - id породы, br_name - название'''

    #Загрузка изображений для породы
    res =  getCatsByBreed(br_id)
    # print(res)
    #строка для размещения и прокрутка 5 фото
    images_row = ft.Row(expand=1,width=500, wrap=False, scroll=ft.ScrollMode.ALWAYS)

    #из полученного рез-та берем 5 фото
    for cat in res[0:5]:
        print(cat['url'])
        images_row.controls.append(
            ft.Image(
                src=cat['url'],
                width=300,
                height=300,
                fit=ft.ImageFit.SCALE_DOWN, ##??Подбирать!!
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text(f"Порода {br_name}"),
        content=images_row,
        actions=[
            ft.TextButton("Закрыть", on_click=lambda e:e.page.close(dlg_modal)),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    #Открываем диалог
    e.page.open(dlg_modal)