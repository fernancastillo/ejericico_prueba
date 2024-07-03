from funciones import *
os.system("cls")
print("Bienvenido a la aplicación de Gaxplosive")
while True:
    print("Presione una tecla para continuar")
    msvcrt.getch()
    os.system("cls")
    print("MENÚ GAXPLOSIVE:")
    print("1. Registrar Pedido")
    print("2. Listar todos los pedidos")
    print("3. Buscar pedido por RUT")
    print("4. Imprimir hoja de ruta")
    print("5. Salir del programa")
    opc=int(input("Ingrese un número del menú: "))
    os.system("cls")
    if opc==1:
        menu_1()
    elif opc==2:
        pass
    elif opc==3:
        pass
    elif opc==4:
        pass
    else:
        print("Muchas gracias por usar la aplicación. Adios!")
        break