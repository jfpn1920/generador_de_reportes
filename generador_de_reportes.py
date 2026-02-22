datos = {
    "ventas enero": 1500,
    "ventas febrero": 2000,
    "ventas marzo": 1750,
    "ventas abril": 2200
}
def mostrar_datos():
    print("\n datos registrados:")
    for clave, valor in datos.items():
        print(f"- {clave}: {valor}")
def generar_reporte():
    if not datos:
        print("no hay datos registrados para generar reporte.")
        return
    valores = list(datos.values())
    total = sum(valores)
    promedio = total / len(valores)
    mayor = max(valores)
    menor = min(valores)
    print("\n resporte estadistico")
    print(f"total: {total}")
    print(f"promedio: {promedio:.2f}")
    print(f"valor mayor: {mayor}")
    print(f"valor menor: {menor}")
def menu():
    while True:
        print("\n generador de reportes ")
        print("1. mostrar datos")
        print("2. generar reporte estadistico")
        print("3. salir")
        opcion = input("seleccione una opcion: ")
        if opcion == "1":
            mostrar_datos()
        elif opcion == "2":
            generar_reporte()
        elif opcion == "3":
            print("saliendo del generador de reportes.")
            break
        else:
            print("opcion invalida, intente nuevamente.")
menu()