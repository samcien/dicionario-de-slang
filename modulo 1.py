import sqlite3

# Función para crear la tabla si no existe
def crear_tabla():
    conn = sqlite3.connect('slang_panameno.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS palabras (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        palabra TEXT NOT NULL,
                        significado TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# Función para agregar una nueva palabra al diccionario
def agregar_palabra():
    palabra = input("Ingrese la nueva palabra: ")
    significado = input("Ingrese el significado de la palabra: ")
    conn = sqlite3.connect('slang_panameno.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO palabras (palabra, significado) VALUES (?, ?)", (palabra, significado))
    conn.commit()
    conn.close()
    print("Palabra agregada exitosamente.")

# Función para editar una palabra existente
def editar_palabra():
    palabra = input("Ingrese la palabra que desea editar: ")
    nuevo_significado = input("Ingrese el nuevo significado de la palabra: ")
    conn = sqlite3.connect('slang_panameno.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE palabras SET significado = ? WHERE palabra = ?", (nuevo_significado, palabra))
    conn.commit()
    conn.close()
    print("Palabra editada exitosamente.")

# Función para eliminar una palabra existente
def eliminar_palabra():
    palabra = input("Ingrese la palabra que desea eliminar: ")
    conn = sqlite3.connect('slang_panameno.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM palabras WHERE palabra = ?", (palabra,))
    conn.commit()
    conn.close()
    print("Palabra eliminada exitosamente.")

# Función para ver el listado de palabras
def ver_listado():
    conn = sqlite3.connect('slang_panameno.db')
    cursor = conn.cursor()
    cursor.execute("SELECT palabra, significado FROM palabras ORDER BY palabra")
    palabras = cursor.fetchall()
    conn.close()

    if not palabras:
        print("El diccionario está vacío.")
    else:
        for palabra, significado in palabras:
            print(f"{palabra}: {significado}")

# Función para buscar el significado de una palabra
def buscar_significado():
    palabra = input("Ingrese la palabra que desea buscar: ")
    conn = sqlite3.connect('slang_panameno.db')
    cursor = conn.cursor()
    cursor.execute("SELECT significado FROM palabras WHERE palabra = ?", (palabra,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        print(f"{palabra}: {resultado[0]}")
    else:
        print("Palabra no encontrada en el diccionario.")

# Función principal para el menú de opciones
def main():
    crear_tabla()
    while True:
        print("\nOpciones:")
        print("a) Agregar nueva palabra")
        print("b) Editar palabra existente")
        print("c) Eliminar palabra existente")
        print("d) Ver listado de palabras")
        print("e) Buscar significado de palabra")
        print("f) Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "a":
            agregar_palabra()
        elif opcion == "b":
            editar_palabra()
        elif opcion == "c":
            eliminar_palabra()
        elif opcion == "d":
            ver_listado()
        elif opcion == "e":
            buscar_significado()
        elif opcion == "f":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
