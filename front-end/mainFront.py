
import flet as ft

def main(page: ft.Page):
    page.title = "Olá, Flet!"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value = "0" , text_align= ft.TextAlign.LEFT, width= 100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plusClick(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE , on_click= minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD , on_click= plusClick),
            ],
            alignment= ft.MainAxisAlignment.CENTER,
        )
    )
    

ft.app(target=main)
