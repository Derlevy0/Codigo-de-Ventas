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
DatosComprador.append(Nom,CC,Dir,Tel)

camisetas = {1: ['Polo','Blanca', 15], 2:['Polo','Azul', 15], 3: ['Polo','Roja', 15], 4: ['Polo','Amarilla', 15], 
             5: ['Cuello redondo','Gris', 12], 6: ['Cuello redondo','Negro', 12], 7: ['Cuello redondo','Verde', 12]}
           
jean = {1: ['Azul', 20], 2:['Verde', 20], 3:['Café', 20], 4: ['Negro', 20], 5: ['Gris', 20]}

zapatos = {1:['Botas','Café', 25], 2: ['Tenis','Azul', 20], 3:['Botas','Negro', 25], 4: ['Tenis','Blanco', 20]}
        
    
        
