DatosComprador=[]
Compras=[]
TotalCompras=[]

print("Ingrese los siguientes datos por favor\n")

Nom = input("Nombres y Apellidos: ")
while True:
    try:
     CC = int(input("Numero de Indentificacion: "))
     break
    except ValueError:
        print("¡Ingrese Solo Valores Numericos!\n") 
Dir = input("Direccion: ")
while True:
    try:
     Tel = int(input("Telefono: "))
     break
    except ValueError:
             print("¡Ingrese Solo Valores Numericos!\n")
        
    
        