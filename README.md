## 👋 ¡Bienvenidos usuarios a mi proyecto! generador de reportes

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de un sistema en Python que genera reportes simples a partir de datos almacenados en diccionarios. El programa permite registrar información y luego calcular estadísticas básicas, ofreciendo una visión resumida de los datos de manera rápida y organizada.

Cada registro se guarda como clave dentro del diccionario, mientras que su valor numérico asociado permite realizar cálculos automáticos, como el total, promedio, valor mayor y valor menor. Esto facilita la generación de reportes precisos sin necesidad de manipular los datos manualmente.

El sistema funciona mediante un menú interactivo en consola, permitiendo al usuario mostrar los datos ingresados o generar un reporte estadístico en cualquier momento, de manera sencilla y práctica.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- Implementar diccionarios para almacenar datos de forma estructurada.
- Aplicar funciones para modularizar el código y organizar la lógica.
- Utilizar bucles `for` para recorrer los registros.
- Calcular estadísticas básicas: total, promedio, valor mayor y valor menor.
- Validar la existencia de datos antes de generar reportes.
- Crear un menú interactivo que permita al usuario administrar la información fácilmente.

#
### 🧠 Temas que se a aplicado
- Diccionarios
- Funciones
- Bucles `for`
- Condicionales (`if`, `else`)
- Operaciones matemáticas (`sum`, `max`, `min`, promedio)
- Validación de existencia de datos
- Menú interactivo con bucle `while`

#
### ⚙️ Funcionamiento
1. Se crea un diccionario llamado `datos` donde:
   - La clave representa el nombre del registro.
   - El valor representa un dato numérico asociado.

2. El menú principal permite:
   - Mostrar todos los datos registrados.
   - Generar un reporte estadístico con:
     - Total de los valores.
     - Promedio.
     - Valor mayor.
     - Valor menor.
   - Salir del sistema.

3. Al generar el reporte, el programa recorre los datos utilizando un bucle `for` y realiza los cálculos automáticamente.

4. El programa se ejecuta continuamente hasta que el usuario decide salir, permitiendo una gestión dinámica y organizada de la información.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```