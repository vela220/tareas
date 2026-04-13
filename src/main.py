import flet as ft
from controllers.UserController import AuthControllerftom
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.dashboard import DashboardView

def main(page: ft.Page):
    #Instanciamos los controladores una sola vez
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
def route_change(route):
    page.views.

