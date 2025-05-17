from cProfile import label
import datetime
import flet as ft

def getButton():
    return ft.ElevatedButton(text="Кнопка",on_click=lambda e:print("Кнопка нажата"))

def main(page:ft.Page):
    page.theme_mode = ft.ThemeMode.SYSTEM

    def onFieldChange(e):
        print(e.control.value)
        txt.value = e.control.value
        txt.update()

    txt = ft.Text('qwe')
    txt1 = ft.Text('qwe')
    
    row = ft.Row(controls=[txt,txt1])
    cnt_row = ft.Container(content=row,bgcolor=ft.Colors.GREEN_300)
    
    page.add(txt)
    page.add(txt1)
    page.add(cnt_row)

    tf = ft.TextField("field", 
                      label='qq',
                      width=150,
                      bgcolor=ft.Colors.GREEN_200,
                      multiline=True,
                      on_change=onFieldChange)
    page.add(tf)

    page.add(
        ft.ElevatedButton(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.open(
                ft.DatePicker(
                    first_date=datetime.datetime(year=2000, month=10, day=1),
                    last_date=datetime.datetime(year=2025, month=10, day=1),

                )
            ),
        )
    )
   
    #Доделать
    # page.add(
    #     ft.Card(
    #         content= ft.Column( [ft.DataTable(
    #         columns=[
    #             ft.DataColumn(ft.Text("First name")),
    #             ft.DataColumn(ft.Text("Last name")),
    #             ft.DataColumn(ft.Text("Age"), numeric=True),
    #         ],
    #         rows=[
    #             ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(ft.Text("John")),
    #                     ft.DataCell(ft.Text("Smith")),
    #                     ft.DataCell(ft.Text("43")),
    #                 ],
    #             ),
    #             ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(ft.Text("Jack")),
    #                     ft.DataCell(ft.Text("Brown")),
    #                     ft.DataCell(ft.Text("19")),
    #                 ],
    #             ),
    #             ft.DataRow(
    #                 cells=[
    #                     ft.DataCell(ft.Text("Alice")),
    #                     ft.DataCell(ft.Text("Wong")),
    #                     ft.DataCell(ft.Text("25")),
    #                 ],
    #             ),
    #         ]
    # ]))),
                
            
            
    #         shadow_color=ft.Colors.ON_SURFACE_VARIANT,
    #     )
    # )
    page.add(getButton())

ft.app(target=main)    