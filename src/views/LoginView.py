import flet as ft

def LoginView(page, auth_contoller):
    email_input = ft.TextField(
        label="Correo electronico", 
        width=350,
        border_radius=10,
        keyboard_type=ft.KeyboardType.EMAIL
        )
    
    pass_input = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350, 
        border_radius=10
        )
    
def login_click(e):
    if not email_input.value or not pass_input.value:
        page.snack_bar = ft.SnackBar(ft.Text("por favor, llene todos los campos"))
        page.snack_bar.open = True
        page.update()
        return
        
    user, msg =auth_controller.login(email_input.value, pass_input.value)
    
    if user:
        page.session.set("user", user) 
        page.go("/dashboard")
    else:
        page.snack_bar = ft.Snackbar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()
        
login_button = ft.ElevetedButton(
    "Entrar"
    on_click=login_click,
    width=350,
    bgcolor="blue",
    color="white"
)

pass_input.on_submit = login_click
        
    return ft.View(
        route"/", 
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAlignment.CENTER,
        appbar=ft.Appbar(
            title=ft.Text("SIGE - login"),
            bgcolor="bluegrey900",
            color="white"
        ),
        controls=[
            ft.Column(
                [
                    ft.text("Acceso al sistema", size=24, weight="bold"),
                    email_input,
                    pass_input,
                    login_button,
                    ft.TextButon(
                        "Crear una cuenta nueva",
                        on_click=lambda _: page.go("/registro")
                    )
                ],
                horizontal_Alignment=ft.CrossAxisAlignment.CENTER,
                tight=True,
                spacing=20
            )
        ]
    )