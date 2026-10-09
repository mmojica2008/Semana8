nombres = input("Dime tus nombres: ")
apellido = input("Dime tu apellido: ")
edad = int(input("Dime tu edad: "))

with open("archivo4.txt", "w") as archivo:
    archivo.write(f"Nombres: {nombres}\n")
    archivo.write(f"Apellido: {apellido}")
    archivo.write(f"Edad: {edad}")
     