#  __________________
#  Import LIBRARIES
import flet as ft
#  Import FILES
#  __________________


def main(page: ft.Page) -> None:
    page.title = "Retail Management System"

    #  AppBar
    page.appbar = ft.AppBar(
        #   -- Logo
        leading=ft.Container(
            content=ft.Row(
                [
                    ft.Text("RMS", weight=ft.FontWeight.BOLD, size=25),
                    ft.Text(
                        "2025",
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.ORANGE_500,
                        size=22,
                        italic=True,
                    ),
                ]
            ),
            padding=ft.Padding(left=14, top=0, right=0, bottom=0),
        ),
        bgcolor=ft.colors.INDIGO_200,
        # title=ft.Text("RMS System - 2025"),
        #  -- NavBar
        actions=[
            ft.Container(
                padding=ft.Padding(left=0, top=0, right=14, bottom=0),
                content=ft.Row(
                    controls=[
                        ft.ElevatedButton("Home", bgcolor=ft.Colors.INDIGO_300),
                        ft.ElevatedButton("Orders", bgcolor=ft.Colors.INDIGO_300),
                        ft.ElevatedButton("Customers", bgcolor=ft.Colors.INDIGO_300),
                        ft.ElevatedButton("Cachier", bgcolor=ft.Colors.INDIGO_300),
                        ft.FilledButton("New Order", bgcolor=ft.Colors.ORANGE),
                        ft.IconButton(icon=ft.Icons.NOTIFICATIONS),
                    ],
                    spacing=8,
                ),
            ),
            # -- Pop Menu
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem("Acount"),
                    ft.PopupMenuItem("Setting"),
                    ft.PopupMenuItem("Help"),
                    ft.PopupMenuItem("Help"),
                ],
            ),
        ],
    )

    #  Main Container
    main_container = ft.Container(expand=True, bgcolor=ft.Colors.INDIGO_400)

    page.add(main_container)


ft.app(target=main)


# random_text = ft.Text("Retail Management System - 2025", size=35, data=0)
# page.add(
#     ft.SafeArea(
#         ft.Container(
#             random_text,
#             alignment=ft.alignment.center,
#         ),
#         expand=True,
#     )
# )
