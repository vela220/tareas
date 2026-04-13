import flet as ft

def LoginView(page, auth_contoller):
    email_input = ft.TextField(label="Correo electronico", width=350, border_radius=10)
    pass_input = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=350, border_raidus=10)
    
def login_click(e):
    user, msg =auth_controller.login(email_imput.value, pass_imput.value)
    if user:
        page.session.set("user", user)#guardamos la sesion
        page.go("/dashboard")
    else:
        page.snack_bar = ft.Snackbar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()
        
    return ft.View("/", [
        ft.AppBar(title=ft.Text("SIGE - login"), bgcolor=ft.Colors.BLUE_GREY_900, COLOR="white"),
        ft.Column([
            ft.Icon(ft.Icons.LOCK_PERSON, size=50, color=ft.Colors.BLUE),
            ft.Text("Acceso al Sistema", size=24, weight="bold"),
            email_imput,
            pass_imput,
            ft.ElevatedButton("Entrar", on_click=login_click, width=350),
            ft.TextButton("Crear una cuenta nueva", on_click=lambda _: page.go("/registro"))
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER)
    ])