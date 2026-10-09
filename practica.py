print("=" * 40)
print("Lectura")
print("=" * 40)

with open("archivos.txt", "r") as archivo:
    contenido = archivo.read()

print("\n Contenido del archivo:")
print("-" * 40)
print(contenido)
print("-" * 40)

print(" Archivo leído correctamente")
print("=" * 40)