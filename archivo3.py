frase = input("Dime tu frase favorita: ")

with open("frase.txt", "w") as archivo:
    archivo.write(frase)

print("Archivo creado satisfactoriamente.")    