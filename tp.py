import flet as ft

def main(page):
    #Definir ancho y altura de la ventana
    page.window_width = 600  #Ancho de la ventana
    page.window_height = 400  #Altura de la ventana
    page.title = "Lista de Compras"  #Título de la ventana
    page.theme_mode = ft.ThemeMode.LIGHT  # Tema claro

    # Función para añadir
    def agregar_opc(e):
        if new_task.value != "":  #Verifica que el campo de texto no esté vacío utilizando if / Si está vacío no agrega la tarea
            task = opciones_tarea(new_task.value)  #Crea una tarjeta de tarea con todos los botones
            task_list.controls.append(task)  #Agrega la tarjeta a la lista de tareas
            new_task.value = ""  #Vacía el campo de texto
            new_task.focus() #Enfoca al campo de texto para agregar otra opción a la lista de tareas
            page.update()

    #Función editar
    def guardar_editado(e, task_checkbox, edit_textbox, task_view, edit_view):
        task_checkbox.label = edit_textbox.value  #Actualiza el texto del checkbox una vez presionado en guardar
        task_checkbox.update()  #Actualiza la vista con la opción modificada
        task_view.visible = True  #Muestra la vista normal de la tarea
        edit_view.visible = False  #Oculta la vista de edición
        page.update()

    #Función para eliminar
    def eliminar_tarea(e, task_card):
        task_list.controls.remove(task_card)  #Elimina la opción de la lista de tareas
        page.update()

    #Crear opciones de tareas con botones de editar y eliminar
    def opciones_tarea(task_text):
        task_checkbox = ft.Checkbox(label=task_text)

        #Vista para mostrar la tarea
        task_view = ft.Row([
            task_checkbox,
            ft.IconButton(icon=ft.icons.EDIT, on_click=lambda e: mostrar_vista_edit(task_view, edit_view)), #icono de editar
            ft.IconButton(icon=ft.icons.DELETE, on_click=lambda e: eliminar_tarea(e, task_card)) #icono de eliminar
        ])

        #Vista para editar la tarea
        edit_textbox = ft.TextField(value=task_text)
        edit_view = ft.Row([
            edit_textbox,
            ft.IconButton(icon=ft.icons.SAVE, on_click=lambda e: guardar_editado(e, task_checkbox, edit_textbox, task_view, edit_view)) #icono de modificar cambios
        ], visible=False)

        #Alterna las vistas de tarea y edición
        def mostrar_vista_edit(task_view, edit_view):
            task_view.visible = False  #Oculta la vista de tarea
            edit_view.visible = True  #Muestra la vista de edición
            page.update()

        #Contenedor que agrupa ambas vistas (tarea y edición)
        task_card = ft.Column([task_view, edit_view]) #Coloca en columna las vistas
        return task_card

    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)  #Campo de texto para añadir nuevas tareas

    #Cabecera con el logo e imagen (texto o imagen)
    logo = ft.Image(src="img/logo.png", width=150, height=150)
    header_text = ft.Text("Moon, lista de compras", size=20, weight=ft.FontWeight.BOLD)

    #Se organiza la cabecera en una columna
    header = ft.Column([
        logo,
        header_text
    ], alignment=ft.MainAxisAlignment.CENTER, 
    horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    #Lista donde se agregarán las tareas
    task_list = ft.Column()

    #Se agregan elementos a la página
    page.add(
        ft.Column([  #Se centra todo el contenido
            header,  #Agrega la cabecera
            ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=agregar_opc)], alignment=ft.MainAxisAlignment.CENTER), #Centra los elementos
            task_list  #Se muestran las tareas
        ], alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.app(main, assets_dir="img")  #Hace que funcione la imagen
