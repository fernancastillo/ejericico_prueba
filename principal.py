from funciones import *
os.system("cls")
print("Bienvenido a la aplicación de Gaxplosive")
while True:
    print("Presione una tecla para continuar")
    msvcrt.getch()
    os.system("cls")
    print("\tMENÚ GAXPLOSIVE:\n")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir del programa")
    while True:
        try:
            opc=int(input("Ingrese un número del menú: "))
            if opc in (1,2,3,4,5):
                break
            else:
                print("Error! Debe ingresa un número del menú!")
        except:
            print("Error! Debe ingresar un número entero!")
    os.system("cls")
    if opc==1:
        menu_1()
    elif opc==2:
        menu_2()
    elif opc==3:
        menu_3()
    elif opc==4:
        menu_4()
    else:
        print("Muchas gracias por usar la aplicación. Adios!")
        break