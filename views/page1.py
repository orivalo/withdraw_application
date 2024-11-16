import flet as ft
from flet_route import Params, Basket
from classes import User, balance
from utils import only_str, on_text_change, capitalize_words, only_int

def Page1(page: ft.Page, params: Params, basket: Basket):
    #Creating the instance and go to nex page
    def on_click_save_and_go():
        name_input = tb1.value
        surname_input = tb2.value
        id_input = tb3.value
        city_input = tb4.value
        user_info = User(name_input, surname_input, id_input, city_input)
        user_info.show_info()
        basket.my_data= {"name":name_input,"surname":surname_input,"id":id_input,"city":city_input}
        page.go("/page2/:test_amount")
    
    # If field is empty filling it with red
    def check_empty_fields():
        fields = [tb1, tb2, tb3, tb4]
        all_filled = False
        
        for field in fields:
            if field.value:
                field.bgcolor = ft.colors.WHITE
                field.filled = False
                all_filled = False
            else:
                field.bgcolor = ft.colors.RED_300
                field.filled = True
            
            field.update()

        if any(not field.value for field in fields):
            all_filled = False
        else:
            all_filled = True
        
        return all_filled

    #If input writed go next page and saving instance
    def check():
        if check_empty_fields():
            on_click_save_and_go()
        else:
            snack = ft.SnackBar("Please fill in all fields!")
            page.add(snack)
            page.update()
    
    
    #Textboxes
    t = ft.Text()
    tb1 = ft.TextField(label="Name", hint_text="Ex: Anna", on_change= lambda e: (capitalize_words(e), on_text_change(e), only_str(e)))
    tb2 = ft.TextField(label="Surname", hint_text="Ex: Krutova", on_change= lambda e: (capitalize_words(e), on_text_change(e), only_str(e)))
    tb3 = ft.TextField(label="ID", hint_text="Ex: 20224871", on_change= lambda e: (capitalize_words(e), on_text_change(e), only_int(e)), max_length = 8)
    tb4 = ft.TextField(label="City", hint_text="Ex: Alsancak", on_change= lambda e: (capitalize_words(e), on_text_change(e), only_str(e)))
    
    

    

    text_fileds_column = ft.Column(
        controls=[tb1, tb2, tb3, tb4],
        spacing=10
    )
    return ft.View(
        "/",
        bgcolor = '#5D6169',
        controls = [
            ft.Container(
                padding=ft.Padding(top=100, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                    content=ft.Text(
                        "Register your Bank Account",\
                            color=ft.colors.BLACK,
                            size=68,
                            weight=ft.FontWeight.BOLD
                    )
            ),      

            ft.Container(
                padding=ft.Padding(top=120, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                content=text_fileds_column ,
            ),

            
            ft.Container(
                padding=ft.Padding(top=250, left=0, right=0, bottom=0),
                alignment=ft.alignment.center,
                content=ft.ElevatedButton(
                    content=ft.Text(
                    "Confirm",
                    weight=ft.FontWeight.BOLD,
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

