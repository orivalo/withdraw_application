import flet as ft
from flet_route import Params, Basket
from utils import on_text_change, only_int, check_empty_single_field
from classes import User, balance

def Page4(page: ft.Page, params: Params, basket: Basket):

    text_field = ft.TextField(label="Value, only integer!", hint_text="Ex: 123", on_change= lambda e: (on_text_change(e), only_int(e)), max_length = 9)

    def handle_close(e):
        page.close(dlg_modal)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Insufficient funds"),
        content=ft.Text(f"You have {basket.get("balance_class")}$ on your balance"),
        actions=[
            ft.TextButton("Confirm", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(
            ft.Text("Modal dialog dismissed"),
        ),
    )

    def user_balance_change_and_go():
        new_user_balance = int(basket.get("balance_class"))-float(text_field.value)
        basket.balance_class = new_user_balance
        page.go("/page5/:completed")

    
    def combined_check_and_value():
        if check_empty_single_field(text_field):
            basket_balance_int = int(basket.get("balance_class"))
            text_field_value = float(text_field.value)
            if text_field_value > basket_balance_int:
                page.open(dlg_modal)
            else:
                user_balance_change_and_go()
        else:
            snack = ft.SnackBar("Please fill in all fields!")
            page.add(snack)
            page.update()


    return ft.View(
        "/page2/:test_amount",
        bgcolor = '#5D6169',
        controls = [
            ft.Container(
                padding=ft.Padding(top=150, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                    content=ft.Text(
                        "Write amount of money that you want to withdraw",
                            color=ft.colors.BLACK,
                            size=68,
                            weight=ft.FontWeight.BOLD
                    )
            ),      
            
            ft.Container(
                padding=ft.Padding(top=70, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                content=text_field 
            ),

            ft.Container(
                padding=ft.Padding(top=350, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                content=ft.ElevatedButton(
                    content=ft.Text(
                    "Withdraw",
                    weight=ft.FontWeight.W_500,
                    size=38,
                    ),
                    on_click=lambda _: combined_check_and_value(),
                    height=100,
                    width=250,
                    style=ft.ButtonStyle(
                        bgcolor= '#658CC2',
                        color= ft.colors.BLACK,
                        padding={ft.MaterialState.HOVERED: 20},
                        overlay_color=ft.colors.TRANSPARENT,
                        elevation={"pressed": 0, "": 1},
                        animation_duration=500
                        
                    )
                )
            )
        ]
    )

