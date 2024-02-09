import flet as ft

def main(page: ft.Page):
    for i in range(200):
        page.controls.append(ft.Text(f"Line {i}"))
    page.scroll = "always"
    page.update()

# ft.app(target=main)
ft.app(target=main, view=ft.AppView.WEB_BROWSER)
