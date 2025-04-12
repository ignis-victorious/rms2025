#  __________________

#  __________________


import flet as ft


def main(page: ft.Page) -> None:
    random_text = ft.Text("Hello World", size=50, data=0)

    page.add(
        ft.SafeArea(
            ft.Container(
                random_text,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)
