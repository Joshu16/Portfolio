import os
import time

c = 'cls'

# Precios y nombres de productos
h1 = 3
h1a = "Hamburguesa Basic"
h2 = 5
h2a = "Hamburqueso"
h3 = 8
h3a = "Hamburguesa Especial"

p1 = 10
p1a = "Pizza Pequeña"
p2 = 14
p2a = "Pizza mediana"
p3 = 20
p3a = "Pizza Grande"

n6 = 5
n6a = "Nuggets de 6"
n10 = 7
n10a = "Nuggets de 10"
n20 = 12
n12a = "Nuggets de 12"

a6 = 6
a12 = 15
a24 = 25

pa1 = 1.50
pa2 = 3
pa3 = 5

precios = []
pedido = []

while True:
    os.system(c)
    print("""MIAMI SHARKS

¡Bienvenido a Miami Sharks!

1. Menú
2. Salir

""")
    
    try:
        op = int(input("¿Qué deseas realizar? "))
    except:
        op = 0

    if op == 1:
        while True:
            os.system(c)
            print ("""Menú:

1. Hamburguesa
2. Pizza
3. Nuggets
4. Alitas de pollo
5. Papas fritas
6. Finalizar pedido
7. Eliminar elemento pedido
8. Volver""")

            try:
                menu = int(input("¿Qué deseas comer? "))
            except:
                menu = 0

            if menu == 1:
                menuh = 0
                while menuh != 4:
                    os.system(c)
                    print("En este momento, su lista se ve así: ")
                    print(pedido, "\n")

                    print ("Qué tipo de hamburguesa quieres?")
                    print ("1. Hamburguesa Basic: 3$")
                    print ("2. Hamburqueso: 5$")
                    print ("3. Hamburguesa Especial: 8$")
                    print ("4. Regresar")

                    try:
                        h = int(input("¿Qué hamburguesa quieres? "))
                    except:
                        h = 0

                    if h == 1:
                        pedido.append(h1a)
                        precios.append(h1)

                    elif h == 2:
                        pedido.append(h2a)
                        precios.append(h2)

                    elif h == 3:
                        pedido.append(h3a)
                        precios.append(h3)
                        
                    elif h == 4:
                        menuh = 4
                    else:
                        print ("Opción incorrecta")
                        time.sleep(1)

            elif menu == 2:
                menup = 0
                while menup != 4: 
                    os.system(c)
                    print ("Qué tipo de pizza quieres?")
                    print ("1. Pizza pequeña: 10$")
                    print ("2. Pizza mediana: 14$")
                    print ("3. Pizza grande: 20$")
                    print ("4. Regresar")
                    try:
                        p = int(input("¿Qué pizza quieres? "))
                    except:
                        p = 0

                    if p == 1:
                        pedido.append(p1a)
                        precios.append(p1)

                    elif p == 2:
                        pedido.append(p2a)
                        precios.append(p2)

                    elif p == 3:
                        pedido.append(p3a)
                        precios.append(p3)

                    elif p == 4:
                        menup = 4
                    else:
                        print("Opción incorrecta")
                        time.sleep(1)

            elif menu == 3:
                while True:
                    os.system(c)
                    print("En este momento, su lista se ve así: ")
                    print(pedido, "\n")

                    print("Qué tipo de nuggets quieres?")
                    print("1. Nuggets de 6: 5$")
                    print("2. Nuggets de 10: 7$")
                    print("3. Nuggets de 12: 12$")
                    print("4. Regresar")
                    try:
                        n = int(input("¿Qué opción eliges? "))
                    except:
                        n = 0

                    if n == 1:
                        pedido.append(n6a)
                        precios.append(n6)
                    elif n == 2:
                        pedido.append(n10a)
                        precios.append(n10)
                    elif n == 3:
                        pedido.append(n12a)
                        precios.append(n20)
                    elif n == 4:
                        break
                    else:
                        print("Opción incorrecta")
                        time.sleep(1)

            elif menu == 4:
                while True:
                    os.system(c)
                    print("Qué cantidad de alitas deseas?")
                    print("1. 6 alitas: 6$")
                    print("2. 12 alitas: 15$")
                    print("3. 24 alitas: 25$")
                    print("4. Regresar")
                    try:
                        a = int(input("¿Qué opción eliges? "))
                    except:
                        a = 0

                    if a == 1:
                        pedido.append("6 Alitas")
                        precios.append(a6)
                    elif a == 2:
                        pedido.append("12 Alitas")
                        precios.append(a12)
                    elif a == 3:
                        pedido.append("24 Alitas")
                        precios.append(a24)
                    elif a == 4:
                        break
                    else:
                        print("Opción incorrecta")
                        time.sleep(1)

            elif menu == 5:
                while True:
                    os.system(c)
                    print("Qué cantidad de papas fritas deseas?")
                    print("1. Porción pequeña: 1.5$")
                    print("2. Porción mediana: 3$")
                    print("3. Porción grande: 5$")
                    print("4. Regresar")
                    try:
                        f = int(input("¿Qué opción eliges? "))
                    except:
                        f = 0

                    if f == 1:
                        pedido.append("Papas pequeñas")
                        precios.append(pa1)
                    elif f == 2:
                        pedido.append("Papas medianas")
                        precios.append(pa2)
                    elif f == 3:
                        pedido.append("Papas grandes")
                        precios.append(pa3)
                    elif f == 4:
                        break
                    else:
                        print("Opción incorrecta")
                        time.sleep(1)

            elif menu == 6:
                os.system(c)
                print("Tu pedido final es:")
                for i in range(len(pedido)):
                    print(f"- {pedido[i]}: ${precios[i]}")
                print(f"\nTotal a pagar: ${sum(precios)}")
                input("\nPresiona ENTER para continuar...")
                break

            elif menu == 7:
                os.system(c)
                if len(pedido) == 0:
                    print("No hay elementos para eliminar.")
                    time.sleep(1)
                    continue
                print("Lista actual de pedido:")
                for i in range(len(pedido)):
                    print(f"{i+1}. {pedido[i]} - ${precios[i]}")
                try:
                    eliminar = int(input("¿Qué número de elemento deseas eliminar? (0 para cancelar): "))
                    if eliminar > 0 and eliminar <= len(pedido):
                        del pedido[eliminar-1]
                        del precios[eliminar-1]
                        print("Elemento eliminado con éxito.")
                    elif eliminar == 0:
                        print("Cancelado.")
                    else:
                        print("Número inválido.")
                except:
                    print("Entrada no válida.")
                time.sleep(2)

            elif menu == 8:
                break

            else:
                print("Opción inválida.")
                time.sleep(1)

    elif op == 2:
        print("Gracias por visitar Miami Sharks. ¡Hasta pronto!")
        time.sleep(2)
        break

    else:
        print("Opción inválida, intenta de nuevo.")
        time.sleep(1)
