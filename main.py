import flet as ft
from flet_route import Routing, path
from views.page1 import Page1
from views.page2 import Page2
from views.page3 import Page3
from views.page4 import Page4
from views.page5 import Page5
from classes import User, balance

#Main function that controls all pages

def main(page: ft.Page):
    
    
    app_routes = [
        path(url ="/", clear = True, view=Page1),
        path(url = "/page2/:test_amount", clear = True, view=Page2),
        path(url = "/page3/:option", clear = True, view=Page3),
        path(url = "/page4/:wd_amount", clear = True, view=Page4),
        path(url = "/page5/:completed", clear = True, view=Page5)
    ]

    Routing(page=page,
            app_routes=app_routes)
    
    
    page.go(page.route)

ft.app(target = main)