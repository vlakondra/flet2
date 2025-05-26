import flet as ft
import pandas as pd

class MyClass:
    def __init__(self,mypage):
        self.mypage:ft.Page = mypage
        self.btn:ft.TextButton=ft.TextButton('mybutton')
        self.btn.on_click=self.onclick

    def onclick(self,e):
        data={
            'id':range(200),
            'val':range(200)
        }
        print(len(self.mypage.controls))
        if len(self.mypage.controls)==2:
            self.mypage.controls.pop(1)

        
        df = pd.DataFrame(data)
        # print(df)
        self.createTable(df)
        print(len(self.mypage.controls))

    def createTable(self,df):    

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
        self.mypage.add(
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
        self.mypage.update()

        



    def create(self):
        self.mypage.add(self.btn)
        self.mypage.update()

def main(page:ft.Page):
    cls = MyClass(page)
    cls.create()



ft.app(target=main)