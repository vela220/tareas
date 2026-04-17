import flet as ft

def DashboardView(page, tarea_controller):
    user = page.session.get("user")
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user['id_usuario']):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t['titulo'], weight=ft.FontWeight.BOLD),
                            subtitle=ft.Text(f"{t['descripcion']} | Prioridad: {t['prioridad']}"),
                            trailing=ft.Badge(
                                content=ft.Text(t['estado']),
                                bgcolor=ft.colors.ORANGE_300
                            )
                        ),padding=10
                        
                    )
                )
            )
        page.update()
        
    txt_titulo = ft.TextField(label="Nueva Tarea", expand=True)
    
    def add_task(e):
        success, msg = tarea_controller.guardar_nueva(
            user['id_usuario'],
            txt_titulo.value,
            "",
            "media",
            "trabajo"
        )
        if success: 
            txt_titulo.value = ""
            refresh()

    return ft.View(
        route="/Dashboard", 
        controls=[            
            ft.AppBar(
                title=ft.Text(f"Bienvenido, {user['nombre']}"),
                actions=[
                    ft.IconButton(
                        icon=ft.Icons.EXIT_TO_APP,
                        on_click=lambda _: page.go("/")
                    )
                ]
            ),
            ft.Column(
                controls=[
                    ft.Row([
                        txt_titulo,
                        ft.FloatingActionButton(
                            icon=ft.Icons.ADD,
                            on_click=add_task
                        )
                    ]),
                    ft.Divider(),
                    ft.Text(
                        "Mis Tareas Pendientes",
                        size=20,
                        weight=ft.FontWeight.BOLD
                    ),
                    lista_tareas
                ],
                expand=True,
                padding=20
            )
        ],
        on_open=lambda _: refresh()
    )