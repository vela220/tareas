import flet as ft
from controllers.UserController import AuthController
from controllers.TareaController import TareaController
from views.LoginView import LoginView
from views.Dashboard import DashboardView

def start(page: ft.page):
    auth_ctrl = AuthController()
    task_ctrl = TareaController()
    
    def route_change(e):
        page.views.clear()
        
        # Caso 1: Login
        if page.route =="/":
            page.add(ft.Text("Caso1"))
            page.views.append(LoginView(page, auth_ctrl))
            
        # Caso 2: Dashboard
        if page.route == "/dashboard":
            page.views.append(DashboardView(page, task_ctrl))
            
        # Caso de seguridad: si algp falla, mostrar texto de error
        if not page.views:
            page.views.append(
                ft.View("/", [ft.Text("Error:Ruta no encontrada o vista vacia")])
            )
            
        page.update()
        
    page.on_route_change = route_change
    # Forzamos la investigacion inicial
    page.go("/")
    
def main():
    # Ejecucion de la app
    ft.app(target-start)
    
if __name__ == "__main__":
    main()
