import flet as ft
from classes import User

#For write only string in textobx
def only_str(e):
    if not e.control.value.isalpha():
        snack = ft.SnackBar("Please enter only letters.")
        e.page.add(snack)
        e.page.update()
        e.control.value = ""
        e.page.update()

#If input inside textbox, filling with grey
def on_text_change(e):
    if e.control.value:
        e.control.filled = True
        e.control.bgcolor = ft.colors.BLUE_GREY_900
    else:
        e.control.filled = False
        e.control.bgcolor = None
    e.page.update()

#All wards start from capital letter
def capitalize_words(e):
    e.control.value = e.control.value.title()
    e.control.update()

#For write only integer value
def only_int(e):
    if not e.control.value.isdigit():
        snack = ft.SnackBar("Please enter only numbers.")
        e.page.add(snack)
        e.page.update()

        e.control.value = ""
        e.page.update()
    
def check_empty_single_field(text_field):
        # Check if the text field is filled
        if text_field.value:
            text_field.bgcolor = ft.colors.WHITE
            text_field.filled = False
            text_field.update()
            return True  # Field is filled
        else:
            text_field.bgcolor = ft.colors.RED_300
            text_field.filled = True
            text_field.update()
            return False