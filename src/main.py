#  __________________
#  Import LIBRARIES
import flet as ft
#  Import FILES
#  __________________


def main(page: ft.Page) -> None:
    page.title = "Retail Management System"
    random_text = ft.Text("Retail Management System - 2025", size=35, data=0)

    #  AppBar
    page.appbar = ft.AppBar(
        leading=ft.Row(
            [
                ft.Text("RMS", weight=ft.FontWeight.BOLD, size=25),
                ft.Text(
                    "2025",
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.ORANGE_500,
                    size=25,
                    italic=True,
                ),
            ]
        ),
        bgcolor=ft.colors.INDIGO_100,
        title=ft.Text("RMS System - 2025"),
        actions=[
            ft.ElevatedButton("Home"),
            ft.ElevatedButton("Order"),
            ft.ElevatedButton("Customers"),
            ft.ElevatedButton("Cachier"),
        ],
    )

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
