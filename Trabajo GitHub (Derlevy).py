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

while True:
    try:
     P = int(input("""Seleccione una Camiseta:
                  1- camisetas[1]
                  2- camisetas[2]
                  3- camisetas[3]
                  4- camisetas[4]
                  5- camisetas[5]
                  6- camisetas[6]
                  7- camisetas[7]\n"""))
     break
    except ValueError:
        print("¡Ingrese Solo Valores Numericos!\n")
        
while True:
    try:
     S = int(input("""Seleccione un Jean:
                      1- jean[1]
                      2- jean[2]
                      3- jean[3]
                      4- jean[4]
                      5- jean[5]\n"""))
     break
    except ValueError:
        print("¡Ingrese Solo Valores Numericos!\n")
                      
while True:
    try:
     T = int(input("""seleccione unos Zapatos:
                      1- zapatos[1]
                      2- zapatos[2]
                      3- zapatos[3]
                      4- zapatos[4]\n"""))
     break
    except ValueError:
        print("¡Ingrese Solo Valores Numericos!\n")
Compras.append(P,S,T)

Total = camisetas[P][2] + jean[S][1] + zapatos[T][2]
TotalCompras.append(Total)

print(DatosComprador)

print(TotalCompras)

print(Total)
        
    
        
