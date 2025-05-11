import flet as ft

import components as comp


# comp.odb.connect()

# comp.odb.create_tables([comp.Person])
# print(comp.odb, comp.Person)


def getTableNames():
    arr = [
        ft.NavigationDrawerDestination(
            label=m,
            data=m,
        )
        for m in comp.models
        if m != "sqlite_sequence" and m != "sqlite_stat1" and m != "person"
    ]
    return arr


getTableNames()


def onChangeDrawer1(e):
    print(e)  ##Поставить фильтр!!
    print(list(comp.models.keys())[int(e.data)])


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
 
    #Обработчик клика по имени таблицы
    def onChangeDrawer(e):
        #Получим имя таблицы по индексу пукта дравера
        table = list(comp.models.keys())[int(e.data)]
        #Безуспешная попытка закрыть дравер
        pagelet.close_drawer()
        pagelet.close_end_drawer()
        pagelet.update()
        page.update()
        #Получим данные выбранной таблицы
        query = (comp.models[table]
                  .select()
                  .limit(10)
                  .dicts()
                )
        #Построим заголовки таблицы на основе метаданных
        header = [
            ft.DataColumn(ft.Text(col, weight=ft.FontWeight.W_600))
            for col in comp.models[table]._meta.columns
        ]
        #Построим строки таблицы на основе запроса
        rows = []
        for row in query:
            cells = [ft.DataCell(ft.Text(str(cell),overflow=ft.TextOverflow.FADE)) for cell in row.values()]
            rows.append(ft.DataRow(cells))
        #Создадим объект Table
        table = ft.DataTable(
            columns=header,
            rows=rows,
            column_spacing=5,
            heading_row_color=ft.colors.BLUE_GREY_100,
            border=ft.border.all(1, ft.colors.BLUE_GREY_200),expand=True
        )
        # и поместим его в контейнер для центрирования
        cont = ft.Container(
                    content=table,
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    
         )
        #Добавим контейнер к странице
        pagelet.content = cont
        pagelet.update()
    #Создадим объект Drawer
    ed = ft.NavigationDrawer(
        position=ft.NavigationDrawerPosition.END,
        on_change=onChangeDrawer,
        controls=getTableNames(),
    )
    #Создадим объект Pagelet
    pagelet = ft.Pagelet(
        appbar=ft.AppBar(
            title=ft.Text("База данных Chinook"), bgcolor=ft.Colors.AMBER_ACCENT
        ),
        content=ft.Container(ft.Text("")),
        bgcolor=ft.Colors.AMBER_100,
        expand=True,
        drawer=ed,
        height=800,
    )
    #Добавим Pagelet к странице
    page.add(pagelet)


ft.app(main)
