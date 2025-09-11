import flet as ft


def main(page: ft.Page):
    counter = ft.Text("0", size=50, data=0)

    def increment_click(e):
        counter.data += 1
        counter.value = str(counter.data)
        counter.update()
    
    def sub_click(e):
        counter.data -= 1
        counter.value = str(counter.data)
        counter.update()

    page.floating_action_button = ft.Row(
        controls=[
            ft.FloatingActionButton(icon=ft.Icons.REMOVE, on_click=sub_click),
            ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=increment_click),
        ],
        alignment=ft.MainAxisAlignment.END,
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )

ft.app(main)
