import flet as ft
from flet_route import Params, Basket
from classes import User, balance

def Page3(page: ft.Page, params: Params, basket: Basket):
    # Button click handler functions
    def button1_click(e):
        print("Withdraw clicked")
        page.go("/page4/10") 

    def button2_click(e):
        print("Check Balance clicked")
        page.open(dlg_modal)

    button1 = ft.ElevatedButton(
        content=ft.Text(
            "Withdraw",
            weight=ft.FontWeight.W_500,
            size=38,
        ),
        on_click=button1_click,
        height=200,
        width=800,
        style=ft.ButtonStyle(
            bgcolor="#D9D9D9",
            color=ft.colors.BLACK,
            padding={ft.MaterialState.HOVERED: 20},
            overlay_color=ft.colors.TRANSPARENT,
            elevation={"pressed": 0, "": 1},
            animation_duration=500
        )
    )
    button1_container = ft.Container(
        content=button1,
        border_radius=ft.BorderRadius(top_left=8, top_right=8,bottom_left=8, bottom_right=8) ,
        padding=10
    )

    # Button 2 with custom styling
    button2 = ft.ElevatedButton(
        content=ft.Text(
            "Check Balance",
            weight=ft.FontWeight.W_500,
            size=38,
        ),
        on_click=button2_click,
        height=200,
        width=800,
        style=ft.ButtonStyle(
            bgcolor="#D9D9D9",
            color=ft.colors.BLACK,
            padding={ft.MaterialState.HOVERED: 20},
            overlay_color=ft.colors.TRANSPARENT, 
            elevation={"pressed": 0, "": 1},
            animation_duration=500
        )
    )
    button2_container = ft.Container(
        content=button2,
        border_radius=ft.BorderRadius(top_left=8, top_right=8,bottom_left=8, bottom_right=8) ,
        padding=10
    )

    # Column for buttons
    buttons_column = ft.Column(
        controls=[button1_container, button2_container],
        spacing=10
    )
       
    def handle_close(e):
        page.close(dlg_modal)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Your balance:"),
        content=ft.Text(f"You have {basket.get("balance_class")}$"),
        actions=[
            ft.TextButton("Confirm", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )

    return ft.View(
        "/page3/:option",
        bgcolor = '#5D6169',
        controls = [

            ft.Container(
                padding=ft.Padding(top=150, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                    content=ft.Text(
                        "Choose option",
                            color=ft.colors.BLACK,
                            size=68,
                            weight=ft.FontWeight.BOLD
                    )
            ),  
            ft.Container(
                padding=ft.Padding(top=130, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                content=buttons_column  
            )
        ]
    )

