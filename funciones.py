import os, msvcrt, csv, time
pedidos=[]
valor_5=12500
valor_15=25500

def menu_1():
    print("REGISTRAR PEDIDO:")
    rut=int(input("Ingrese el RUT: "))
    nombre=input("Ingrese solamente el nombre del comprador: ")
    direccion=input("Ingrese la dirección: ")
    comuna=int(input("Ingrese el número de la comuna (1. Puente Alto - 2. San Bernardo - 3. San Joaquín): "))
    cont_5=0
    cont_15=0
    while True:
        print("MENÚ CILINDROS")
        print("1. Agregar cilindro de 5 kg. ($ 12.500 c/u)")
        print("2. Eliminar un cilindro de 5 kg.")
        print("3. Agregar cilindro de 15 kg. ($ 25.500 c/u)")
        print("4. Eliminar cilindro de 15 kg.")
        print("5. Ver pedido actual")
        print("6. Continuar")
        opc_2=int(input("Ingrese un número del menú: "))
        if opc_2==1:
            cont_5+=1
            print("Cilindro agregado con éxito!")
            time.sleep (2)
        elif opc_2==2:
            if cont_5==0:
                print("Error! Primero debe agregar un cilindro!")
            else:
                cont_5-=1
                print("Cilindro eliminado con éxito!")
            time.sleep (2)
        elif opc_2==3:
            cont_15+=1
            print("Cilindro agregado con éxito!")
            time.sleep (2)
        elif opc_2==4:
            if cont_15==0:
                print("Error! Primero debe agregar un cilíndro!")
            else:
                cont_15-=1
                print("Cilindro eliminado con éxito!")
            time.sleep (2)
        elif opc_2==5:
            print("PEDIDO ACTUAL:")
            print(f"Cilindros de 5 kg: {cont_5} - Cilindros de 15 kg {cont_15} - Total: $ {valor_5*cont_5+valor_15*cont_15}.")
        else:
            break
        if comuna==1:
            comuna="Puente Alto"
        elif comuna==2:
            comuna="San Bernardo"
        else:
            comuna="San Joaquín"
        pedido={"rut":rut, 
                "nombre":nombre, 
                "comuna":comuna,
                "cil. 5kg":cont_5, 
                "cil. 15kg":cont_15, 
                "total": valor_5*cont_5+valor_15*cont_15}
        pedidos.append(pedido)
        print("Pedido añadido con éxito!")
        