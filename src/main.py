import flet as ft

arr = [1,2,3]
def main(page:ft.Page):
    def changeTxt(e,v):
        print(e)
        txt.value=v
        page.update()

    txt = ft.Text(value="")
    for x in arr:
        page.add(ft.TextButton(x, data=x, on_click=lambda e,v=x: changeTxt(e,v)))

    page.add(txt)
ft.app(target=main)