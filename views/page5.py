import flet as ft
from flet_route import Params, Basket

def Page5(page: ft.Page, params: Params, basket: Basket):
 # Button click handler functions
    def button1_click(e):
        print("Withdraw clicked")
        page.go("/page4/10") 

    def button2_click(e):
        print("Change Balance clicked")
        page.go("/page2/10")

    def button3_click(e):
        print("Close clicked")
        page.window_close()
    
    button1 = ft.ElevatedButton(
        content=ft.Text(
            "Withdraw more",
            weight=ft.FontWeight.W_500,
            size=38,
        ),
        on_click=button1_click,
        height=100,
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
            "Change Balance",
            weight=ft.FontWeight.W_500,
            size=38,
        ),
        on_click=button2_click,
        height=100,
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

    button3 = ft.ElevatedButton(
        content=ft.Text(
            "Close",
            weight=ft.FontWeight.W_500,
            size=38,
        ),
        on_click=button3_click,
        height=100,
        width=250,
        style=ft.ButtonStyle(
            bgcolor="#658CC2",
            color=ft.colors.BLACK,
            padding={ft.MaterialState.HOVERED: 20},
            overlay_color=ft.colors.TRANSPARENT,
            elevation={"pressed": 0, "": 1},
            animation_duration=500
        )
    )
    button3_container = ft.Container(
        content=button3,
        border_radius=ft.BorderRadius(top_left=8, top_right=8, bottom_left=8, bottom_right=8),
        padding=10,
        alignment=ft.alignment.center  # Align the button in the center horizontally
    )
    # Column for buttons
    buttons_column = ft.Column(
        controls=[button1_container, button2_container],
        spacing=10
    )

    return ft.View(
        "/page3/:option",
        bgcolor = '#5D6169',
        controls = [

            ft.Container(
                padding=ft.Padding(top=50, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                    content=ft.Text(
                        "Withdrawal successufully completed",
                            color=ft.colors.BLACK,
                            size=68,
                            weight=ft.FontWeight.BOLD
                    )
            ),  
            ft.Container(
                padding=ft.Padding(top=60, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                content=buttons_column  
            ),
            ft.Container(
                padding=ft.Padding(top=100, left=0, right=0, bottom=0),
                content=button3_container,
                alignment=ft.alignment.bottom_center
            )
        ]
    )

