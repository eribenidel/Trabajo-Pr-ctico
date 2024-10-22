- - - - - - 
Se añade una validación para evitar agregar tareas vacías: if 
new_task.value != "". 
Se crea opciones de tarea mediante la función 
opciones_tarea(task_text) 
Se agrega la funcionalidad de editar tareas. Al presionar el botón de 
edición, aparece un campo de texto para modificar el contenido de la 
tarea, y luego un botón de "guardar" para confirmar los cambios. 
Se añade un botón de eliminar tarea en cada opción, lo que no estaba 
disponible en el código original. 
Se organiza cada tarea dentro de una tarjeta que incluye opciones 
adicionales (editar y eliminar). 
Se utiliza una columna (task_list = ft.Column()) donde se almacenan 
todas las tareas. 
