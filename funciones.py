import os, msvcrt, csv, time
pedidos=[]
valor_5=12500
valor_15=25500
def menu_1():
    print("\tREGISTRAR PEDIDO:\n")
    while True:
        try:
            rut=int(input("Ingrese el RUT (sin guión ni digito verificador): "))
            if len(str(rut))==8 or len(str(rut))==7:
                break
            else:
                print("Error! Debe ingresar 7 u 8 dígitos!")
        except:
            print("Error! Debe ingresar un número entero!")
    while True:
        nombre=input("Ingrese solamente el nombre del comprador: ")
        if len(nombre)<3:
            print("Error! Debe ingresar mínimo 3 caracteres!")
        elif not nombre.isalpha():
            print("Error! Debe ingresar solo letras!")
        else:
            break
    while True:
        direccion=input("Ingrese la dirección: ")
        if len(direccion)<5:
            print("Error! Debe ingresar mínimo 5 caracteres!")
        else:
            break
    while True:
        try:
            comuna=int(input("Ingrese el número de la comuna (1. Puente Alto - 2. San Bernardo - 3. San Joaquín): "))
            if comuna in (1,2,3):
                break
            else:
                print("Error! Debe ingresar un número del 1 al 3!")
        except:
            print("Error! Debe ingresar un número entero!")
    cont_5=0
    cont_15=0
    print("A continuación se ingresará a un menú para agregar cilindros")
    print("Presione una tecla para continuar")
    msvcrt.getch()
    while True:
        os.system("cls")
        print("\tMENÚ CILINDROS:\n")
        print("1. Agregar cilindro de 5 kg. ($ 12.500 c/u)")
        print("2. Eliminar un cilindro de 5 kg.")
        print("3. Agregar cilindro de 15 kg. ($ 25.500 c/u)")
        print("4. Eliminar cilindro de 15 kg.")
        print("5. Ver pedido actual")
        print("6. Terminar pedido")
        while True:
            try:
                opc_2=int(input("Ingrese un número del menú: "))
                if opc_2 in (1,2,3,4,5,6):
                    break
                else:
                    print("Error! Debe ingresar un número del menú!")
            except:
                print("Error! Debe ingresar un número entero!")
        os.system("cls")
        if opc_2==1:
            cont_5+=1
            print("Cilindro agregado con éxito!")
            time.sleep (1)
        elif opc_2==2:
            if cont_5==0:
                print("Error! Primero debe agregar un cilindro!")
            else:
                cont_5-=1
                print("Cilindro eliminado con éxito!")
            time.sleep (1)
        elif opc_2==3:
            cont_15+=1
            print("Cilindro agregado con éxito!")
            time.sleep (1)
        elif opc_2==4:
            if cont_15==0:
                print("Error! Primero debe agregar un cilíndro!")
            else:
                cont_15-=1
                print("Cilindro eliminado con éxito!")
            time.sleep (1)
        elif opc_2==5:
            print("\tPEDIDO ACTUAL:\n")
            print(f"Cilindros de 5 kg: {cont_5} - Cilindros de 15 kg {cont_15} - Total: $ {valor_5*cont_5+valor_15*cont_15}.\n")
            print("Presione una tecla para continuar")
            msvcrt.getch()
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
            "direccion":direccion, 
            "comuna":comuna,
            "cil_5kg":cont_5, 
            "cil_15kg":cont_15, 
            "total": valor_5*cont_5+valor_15*cont_15}
    pedidos.append(pedido)
    print("Pedido agregado con éxito!")
def menu_2():
    print("\tLISTAR TODOS LOS PEDIDOS:\n")
    for p in pedidos:
        print(f"RUT: {p['rut']} - Nombre: {p['nombre']} - Dirección: {p['direccion']} - Comuna: {p['comuna']} - Cil. 5 kg: {p['cil_5kg']} - Cil. 15 kg: {p['cil_15kg']} - Total: {p['total']}")

def menu_3():
    if len(pedidos)==0:
        print("Error! Aún no hay pedidos agregados!")
    else:
        print("\tBUSCAR PEDIDO POR RUT:\n")
        while True:
            try:
                rut=int(input("Ingrese el RUT (sin guión ni digito verificador): "))
                if len(str(rut))==8 or len(str(rut))==7:
                    break
                else:
                    print("Error! Debe ingresar 7 u 8 dígitos!")
            except:
                print("Error! Debe ingresar un número entero!")
        existe=False
        for p in pedidos:
            if p['rut']==rut:
                print(f"RUT: {p['rut']} - Nombre: {p['nombre']} - Dirección: {p['direccion']} - Comuna: {p['comuna']} - Cil. 5 kg: {p['cil_5kg']} - Cil. 15 kg: {p['cil_15kg']} - Total: {p['total']}\n")
                existe=True
        if existe==False:
            print("Error! No se ha encontrado el RUT ingresado!")
def menu_4():
    if len(pedidos)==0:
        print("Error! Aún no hay pedidos agregados!")
    else:
        print("\tIMPRIMIR HOJA DE RUTA\n")
        while True:
            try:
                ruta=int(input("Ingrese el número de la comuna (1. Puente Alto - 2. San Bernardo - 3. San Joaquín): "))
                if ruta in (1,2,3):
                    break
                else:
                    print("Error! Debe ingresar un número del 1 al 3!")
            except:
                print("Error! Debe ingresar un número entero!")
        if ruta==1:
            ruta="Puente Alto"
        elif ruta==2:
            ruta="San Bernardo"
        else:
            ruta="San Joaquín"
        try:
            nombre=input("Ingrese nombre del archivo: ")
            if len(nombre)<3:
                print("Error! Debe ingresar mínimo 3 caracteres!")
            else:
                existe=False
                with open (f"{nombre}.csv", "x", newline="") as archivo:
                    escritor=csv.DictWriter(archivo,['rut', 'nombre','direccion','comuna','cil_5kg','cil_15kg','total'])
                    escritor.writeheader()
                    for p in pedidos:
                        if p['comuna']==ruta:
                            escritor.writerow(p)
                            existe=True
                    if existe==False:
                        print("Archivo creado, pero aún no existen rutas a esa comuna!")
                    elif existe==True:
                        print("Archivo creado con éxito!")
        except:
            print("Error! Ya existe un archivo ingresado con ese nombre!")
