import flet as ft

# class Pagination(ft.UserControl):
class Pagination(ft.Row):
    def __init__(self, total_items:int, items_per_page:int=10, on_page_change=None):
        super().__init__()
        self.total_items = total_items
        self.items_per_page = items_per_page
        self.on_page_change = on_page_change
        self.current_page = 1
        self.total_pages = max(1, (self.total_items + self.items_per_page - 1) // self.items_per_page)
        self.expand = False
        self.width=200

    def build(self):
        self.prev_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            disabled=self.current_page == 1,
            on_click=self.go_prev,
            tooltip="Previous page"
        )
        self.next_button = ft.IconButton(
            icon=ft.icons.ARROW_FORWARD,
            disabled=self.current_page == self.total_pages,
            on_click=self.go_next,
            tooltip="Next page"
        )
        self.page_info = ft.Text(f"Page {self.current_page} of {self.total_pages}")

        # self.buttons_row = ft.Row(
        #     controls=[self.prev_button, self.page_info, self.next_button],
        #     alignment=ft.MainAxisAlignment.CENTER,
        #     vertical_alignment=ft.CrossAxisAlignment.CENTER,
        #     spacing=10,
        #     expand=False
        # )
        self.buttons_row =  self
        self.buttons_row.controls = [self.prev_button, self.page_info, self.next_button]
        self.buttons_row.alignment = ft.MainAxisAlignment.CENTER
        self.buttons_row.spacing=10

        return self.buttons_row

    def go_prev(self, e):
        if self.current_page > 1:
            self.current_page -= 1
            self.update_ui()
            if self.on_page_change:
                self.on_page_change(self.current_page)

    def go_next(self, e):
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.update_ui()
            if self.on_page_change:
                self.on_page_change(self.current_page)

    def update_ui(self):
        self.prev_button.disabled = self.current_page == 1
        self.next_button.disabled = self.current_page == self.total_pages
        self.page_info.value = f"Page {self.current_page} of {self.total_pages}"
        self.update()

    def reset(self, total_items=None):
        if total_items is not None:
            self.total_items = total_items
            self.total_pages = max(1, (self.total_items + self.items_per_page - 1) // self.items_per_page)
        self.current_page = 1
        self.update_ui()

