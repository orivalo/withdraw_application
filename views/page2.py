import flet as ft
from flet_route import Params, Basket
from utils import on_text_change, only_int, check_empty_single_field
from classes import User, balance

def Page2(page: ft.Page, params: Params, basket: Basket):

    text_field = ft.TextField(label="Value, only integer!", hint_text="Ex: 123", on_change= lambda e: (on_text_change(e), only_int(e)), max_length = 9)

    def test_balance_and_go():
        balance_input = text_field.value 
        name_user = basket.my_data.get("name")
        surname_user = basket.my_data.get("surname")
        id_user = basket.my_data.get("id")
        city_user = basket.my_data.get("city")

        user_balance_instance = balance(name=name_user, surname=surname_user, id=id_user, city=city_user, user_balance=balance_input)
        user_balance_instance.show_info()
        print(user_balance_instance.get_balance())
        basket.balance_class = user_balance_instance.get_balance()
        page.go("/page3/10")


    def check():
        if check_empty_single_field(text_field):
            test_balance_and_go()
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
                        "Write test amount of money that will be on your balance",
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
                    "Confirm",
                    weight=ft.FontWeight.W_500,
                    size=38,
                    ),
                    on_click=lambda _: check(),
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

