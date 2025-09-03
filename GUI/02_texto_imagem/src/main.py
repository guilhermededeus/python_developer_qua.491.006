import flet as ft


def main(page: ft.Page):
    page.title = "Meu primeiro app flet"
    page.scroll = "adaptive"
    page.add(
        ft.SafeArea(
            ft.Container(
                ft.Text("Olá, mundo!",size=30,weight="bold")
            ),
            expand=True,
        ),
        ft.Image(
        src="/foto.jpg",
        fit=ft.ImageFit.CONTAIN,
        error_content=ft.Text("Foto de desenvolvedor"),
        width=600
        )
    )


ft.app(target=main)
