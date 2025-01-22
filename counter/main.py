import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"  
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.add(ft.SafeArea(ft.Text("Hello, Flet!")))

txt


ft.app(main)
