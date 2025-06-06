op = 0
puntos = 2000
c = 'cls'


"""Importación función random"""
import random

"""Importación función random"""
import time
"""Importación Operating Sistem"""
import os
"""Importación Operating Sistem"""
import threading
import keyboard

while op != 11:

    if puntos <=0:
        print("\033[1;31m" + "¡Has perdido el simulador de Juegos!")
        print ("¡Gracias por jugar!")
        time.sleep(2)
        exit()
    
    """Simular juegos"""
    print("\033[0;0m" + "-------------------------------------------------------------------------------")
    print("\033[1;36m" + "\033[1;40m" + "Simulación de juegos" + "\033[0;0m" + "\n")

    print ("\033[1;36m" + "\033[1;40m" + "¿Qué juego vas a jugar?" + "\033[0;0m" + "\n")
    print ("""
1. Piedra, Papel o Tijera
   +250  -500
           
2. Ruleta Rusa (Fácil)
   +200  -1000

3. Ruleta Rusa (Medio)
   +500  -1000
           
4. Ruleta Rusa (Difícil)
   +1000 -1000
           
5. Carrera de Caballos
   +1500 -500
           
6. Juego de las frases (Juego de la galleta)
   +1500 -500

7. Juego Luz Roja Luz verde
   +5000 -Pérdida Total
           
10. Salir \n""")
    print ("PUNTAJE:",puntos)

    print("\033[0;0m" + "-------------------------------------------------------------------------------")
    op = int(input("¿Qué deseas realizar? "))

    if op == 1:
        os.system(c)
        """Simular el juego de Piedra Papel o tijera en PYTHON"""
        print("\n\033[1;36m" + "\033[1;40m" + "PIEDRA PAPEL O TIJERA" + "\033[0;0m" + "\n")
        print("Bienvenido, para jugar deberás ingresar una opción entre piedra, papel o tijera. ¡Mucha suerte! \n")

        """Creación lista de opciones"""

        opciones = ["piedra", "papel", "tijera"]

        """Solicitud de opción"""

        usuario = input("Elige: ").lower()
        respuesta = random.choice(opciones)

        print ("\nMi opción es:",respuesta)

        if usuario not in opciones:
            print ("Respuesta no válida")
            quit()

        if usuario == respuesta:
            print("¡Empate!")
            time.sleep(1)

        elif usuario == "tijera" and respuesta == "piedra" or usuario == "piedra" and respuesta == "papel" or usuario == "papel" and respuesta == "tijera":
            print("\033[1;31m" + "¡Has perdido!")
            puntos = puntos - 500
            time.sleep(1)
            print("-500")

        else:
            print("\033[1;32m" + "¡Has ganado!")
            time.sleep(1)
            puntos = puntos + 250
            print("+250")

    
    elif op == 2:

        os.system(c)

        """Simular el juego Ruleta Rusa en PYTHON"""
        print("\033[1;36m" + "\033[1;40m" + "Ruleta Rusa" + "\033[0;0m" + "\n")
        print("Bienvenido, para jugar deberás ingresar un número del 1 al 10, la pistola tendrá una bala, si la bala está en el número que elegiste, morirás. ¡Mucha suerte!\n")


        opciones2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """Solicitud de opción"""

        usuario2 = int(input("Elige un número del 1 al 10: ").lower())
        respuestas2 = random.choice(opciones2)
        
        if usuario2 >10 or usuario2 == 0:
            print ("Escogiste un número inválido")
            quit()

        if respuestas2 == 1:
            print("1: ❌")
        else:
            print("1: ✅")

        time.sleep(1)
            
        if respuestas2 == 2:
            print("2: ❌")
        else:
            print("2: ✅")

        time.sleep(1)
 
        if respuestas2 == 3:
            print("3: ❌")
        else:
            print("3: ✅")

        time.sleep(1)
 
        if respuestas2 == 4:
            print("4: ❌")
        else:
            print("4: ✅")

        time.sleep(1)
 
        if respuestas2 == 5:
            print("5: ❌")
        else:
            print("5: ✅")

        time.sleep(1)
 
        if respuestas2 == 6:
            print("6: ❌")
        else:
            print("6: ✅")

        time.sleep(1)
 
        if respuestas2 == 7:
            print("7: ❌")
        else:
            print("7: ✅")

        time.sleep(1)
 
        if respuestas2 == 8:
            print("8: ❌")
        else:
            print("8: ✅")

        time.sleep(1)
 
        if respuestas2 == 9:
            print("9: ❌")
        else:
            print("9: ✅")

        time.sleep(1)
 
        if respuestas2 == 10:
            print("10: ❌")
        else:
            print("10: ✅")

        time.sleep(1)
 
        if usuario2 == respuestas2:
            print ("\n\033[1;31m" + "Has sido asesinado, perdiste...")
            puntos = puntos - 1000
            time.sleep(1)
            print("-1000")
        elif usuario2 != respuestas2 and usuario2 <11:
            print ("\n\033[1;32m" + "Te salvaste, ganaste!")
            puntos = puntos + 200
            time.sleep(1)
            print("+200")

    elif op == 3:
        os.system(c)

        """Simular el juego Ruleta Rusa en PYTHON"""
        print("\033[1;36m" + "\033[1;40m" + "Ruleta Rusa Nivel Medio" + "\033[0;0m" + "\n")
        print("Bienvenido, para jugar deberás ingresar un número del 1 al 10, la pistola tendrá tres balas, si la bala está en el número que elegiste, morirás. ¡Mucha suerte!\n")

        opciones4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """Solicitud de opción"""

        usuario4 = int(input("Elige un número del 1 al 10: ").lower())
        respuestas4 = random.choice(opciones4)
        respuestas4a = random.choice(opciones4)
        respuestas4b = random.choice(opciones4)
        
        if respuestas4 == 1 or respuestas4a == 1 or respuestas4b == 1:
            print("1: ❌")
        else:
            print("1: ✅")

        time.sleep(1)

        if respuestas4 == 2 or respuestas4a == 2 or respuestas4b == 2:
            print("2: ❌")
        else:
            print("2: ✅")

        time.sleep(1)

        if respuestas4 == 3 or respuestas4a == 3 or respuestas4b == 3:
            print("3: ❌")
        else:
            print("3: ✅")

        time.sleep(1)

        if respuestas4 == 4 or respuestas4a == 4 or respuestas4b == 4:
            print("4: ❌")
        else:
            print("4: ✅")

        time.sleep(1)

        if respuestas4 == 5 or respuestas4a == 5 or respuestas4b == 5:
            print("5: ❌")
        else:
            print("5: ✅")

        time.sleep(1)

        if respuestas4 == 6 or respuestas4a == 6 or respuestas4b == 6:
            print("6: ❌")
        else:
            print("6: ✅")

        time.sleep(1)

        if respuestas4 == 7 or respuestas4a == 7 or respuestas4b == 7:
            print("7: ❌")
        else:
            print("7: ✅")

        time.sleep(1)

        if respuestas4 == 8 or respuestas4a == 8 or respuestas4b == 8:
            print("8: ❌")
        else:
            print("8: ✅")

        time.sleep(1)

        if respuestas4 == 9 or respuestas4a == 9 or respuestas4b == 9:
            print("9: ❌")
        else:
            print("9: ✅")

        time.sleep(1)

        if respuestas4 == 10 or respuestas4a == 10 or respuestas4b == 10:
            print("10: ❌")
        else:
            print("10: ✅")

        time.sleep(1)
 
        if usuario4 == respuestas4 or usuario4 == respuestas4a or usuario4 == respuestas4b:
            print ("\n\033[1;31m" + "Has sido asesinado, perdiste...")
            puntos = puntos - 1000
            print("-1000")
            time.sleep(1)
        elif usuario4 != respuestas4 and usuario4 != respuestas4a and usuario4 != respuestas4b and usuario4 <11:
            print ("\n\033[1;32m" + "Te salvaste, ganaste!")
            puntos = puntos + 500
            print("+500")
            time.sleep(1)

    elif op == 4:
        os.system(c)

        """Simular el juego Ruleta Rusa en PYTHON"""
        print("\033[1;36m" + "\033[1;40m" + "Ruleta Rusa Nivel Difícil" + "\033[0;0m" + "\n")
        print("Bienvenido, para jugar deberás ingresar un número del 1 al 10, la pistola tendrá tres balas, si la bala está en el número que elegiste, morirás. ¡Mucha suerte!\n")

        opciones5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        """Solicitud de opción"""

        usuario5 = int(input("Elige un número del 1 al 10: ").lower())
        respuestas5 = random.choice(opciones5)
        respuestas5a = random.choice(opciones5)
        respuestas5b = random.choice(opciones5)
        respuestas5c = random.choice(opciones5)
        respuestas5d = random.choice(opciones5)
        
        if respuestas5 == 1 or respuestas5a == 1 or respuestas5b == 1 or respuestas5c == 1 or respuestas5d == 1:
            print("1: ❌")
        else:
            print("1: ✅")

        time.sleep(1)

        if respuestas5 == 2 or respuestas5a == 2 or respuestas5b == 2 or respuestas5c == 2 or respuestas5d == 2:
            print("2: ❌")
        else:
            print("2: ✅")

        time.sleep(1)

        if respuestas5 == 3 or respuestas5a == 3 or respuestas5b == 3 or respuestas5c == 3 or respuestas5d == 3:
            print("3: ❌")
        else:
            print("3: ✅")

        time.sleep(1)

        if respuestas5 == 4 or respuestas5a == 4 or respuestas5b == 4 or respuestas5c == 4 or respuestas5d == 4:
            print("4: ❌")
        else:
            print("4: ✅")

        time.sleep(1)

        if respuestas5 == 5 or respuestas5a == 5 or respuestas5b == 5 or respuestas5c == 5 or respuestas5d == 5:
            print("5: ❌")
        else:
            print("5: ✅")

        time.sleep(1)

        if respuestas5 == 6 or respuestas5a == 6 or respuestas5b == 6 or respuestas5c == 6 or respuestas5d == 6:
            print("6: ❌")
        else:
            print("6: ✅")

        time.sleep(1)

        if respuestas5 == 7 or respuestas5a == 7 or respuestas5b == 7 or respuestas5c == 7 or respuestas5d == 7:
            print("7: ❌")
        else:
            print("7: ✅")

        time.sleep(1)

        if respuestas5 == 8 or respuestas5a == 8 or respuestas5b == 8 or respuestas5c == 8 or respuestas5d == 8:
            print("8: ❌")
        else:
            print("8: ✅")

        time.sleep(1)

        if respuestas5 == 9 or respuestas5a == 9 or respuestas5b == 9 or respuestas5c == 9 or respuestas5d == 9:
            print("9: ❌")
        else:
            print("9: ✅")

        time.sleep(1)

        if respuestas5 == 10 or respuestas5a == 10 or respuestas5b == 10 or respuestas5c == 10 or respuestas5d == 10:
            print("10: ❌")
        else:
            print("10: ✅")

        time.sleep(1)
 
        if usuario5 == respuestas5 or usuario5 == respuestas5a or usuario5 == respuestas5b or usuario5 == respuestas5c or usuario5 == respuestas5d:
            print ("\n\033[1;31m" + "Has sido asesinado, perdiste...")
            puntos = puntos - 1000
            print("-1000")
            time.sleep(1)
        
        elif usuario5 != respuestas5 and usuario5 != respuestas5a and usuario5 != respuestas5b and usuario5 != respuestas5c and usuario5 != respuestas5d and usuario5 <11:
            print ("\n\033[1;32m" + "Te salvaste, ganaste!")
            puntos = puntos + 1000
            print("+1000")
            time.sleep(1)
    
    elif op == 5:
        os.system(c)
        """Simular el juego Carrera de Caballos en PYTHON"""
        print("\033[1;36m" + "\033[1;40m" + "Carrera de caballos" + "\033[0;0m" + "\n")

        usuario3 = int(input("A qué caballo quieres apostarle del uno al 10: ").lower())
        if usuario3 >10 or usuario3 == 0:
            print ("¡Escogiste un caballo que no participa!")
            quit()
            
        caballo1 = "1🐴"
        caballo2 = "2🐎"
        caballo3 = "3🏇"
        caballo4 = "4🐴"
        caballo5 = "5🐎"
        caballo6 = "6🏇"
        caballo7 = "7🐴"
        caballo8 = "8🐎"
        caballo9 = "9🏇"
        caballo10 = "0🐴"

        win = 0

        while win == 0:
            os.system(c)

            caballos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            print("Apostado: ", usuario3, "\n")
            print("\033[0;0m" + "-------------------------------------------------------------------------------")
            print("                                                                           META")
            print(caballo1)
            print(caballo2)
            print(caballo3)
            print(caballo4)
            print(caballo5)
            print(caballo6)
            print(caballo7)
            print(caballo8)
            print(caballo9)
            print(caballo10)
            print("\033[0;0m" + "-------------------------------------------------------------------------------")

            salto = random.choice(caballos)
            
            if 1 == salto:
                caballo1 = " " + caballo1

            if 2 == salto:
                caballo2 = " " + caballo2

            if 3 == salto:
                caballo3 = " " + caballo3

            if 4 == salto:
                caballo4 = " " + caballo4

            if 5 == salto:
                caballo5 = " " + caballo5

            if 6 == salto:
                caballo6 = " " + caballo6

            if 7 == salto:
                caballo7 = " " + caballo7

            if 8 == salto:
                caballo8 = " " + caballo8

            if 9 == salto:
                caballo9 = " " + caballo9

            if 10 == salto:
                caballo10 = " " + caballo10
            

            if len(caballo1) == 79:
                win = 1

            if len(caballo2) == 79:
                win = 2

            if len(caballo3) == 79:
                win = 3

            if len(caballo4) == 79:
                win = 4

            if len(caballo5) == 79:
                win = 5

            if len(caballo6) == 79:
                win = 6

            if len(caballo7) == 79:
                win = 7

            if len(caballo8) == 79:
                win = 8

            if len(caballo9) == 79:
                win = 9

            if len(caballo10) == 79:
                win = 10

            time.sleep(0.05)

        print ("Usted apostó a:", usuario3,"y ganó:", win)
        if win == usuario3:
            print("\033[1;32m" + "¡Has ganado!")
            puntos = puntos + 1500
            print("+1500 \n")
        else:
            print("\033[1;31m" + "¡Has perdido!")
            puntos = puntos - 500
            print("-500 \n")
        
        time.sleep(2)


    elif op == 6:
        os.system(c)
        print ("\033[1;36m" + "\033[1;40m" + "Juego de la frase" + "\033[0;0m" + "\n")
        frases = ["El amor es el mejor arma contra el enemigo.", "La vida es una cuestión de amor y de amiga.", "El amor es la fuerza que nos unimos.", "El amor es la razón por la que vivimos.", "El amor es la causa de nuestra felicidad.", "El amor es el camino a la felicidad"]
        frase = random.choice(frases)
        #La persona tiene que escribir la frase selecta
        print ("Frase:", frase,)
        print("\n")

        respuesta = input("Escribe la frase ").lower()


        print ("\nTu respuesta fue:", respuesta)
        print ("Frase original:", frase)
        if respuesta == frase.lower():
            print("\033[1;32m" + "\n¡Has ganado!")
            puntos = puntos + 1500
            print("+1500 \n")
        else:
            print("\033[1;31m" + "\n¡Has perdido!")
            puntos = puntos - 500
            print("-500 \n")
        time.sleep(2)

    elif op == 7:
        os.system(c)
        print ("\n\033[1;1m" + "\033[1;40m" + "Juego" "\033[31m" + " Luz Roja" "\033[32m" + " Luz verde" + "\033[0;0m" + "\n")

        num = input("Ingresa el número con el que quieres participar menor de 10 ")

        while len(num) > 1 or num == "1" or num == "2":
            print("Numero inválido, escoge otro")
            num = input("Ingresa el número con el que quieres participar ")

        estado = 1
        usuario = num+"𖧱"
        jugador1 = "1𖧱"
        estado1 = 1
        jugador2 = "2𖧱"
        estado2 = 1
        win2 = 2
        opciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        saltos = [" ", "", "  ", "   ", "", ""]
        Robot = "\033[32m" + "                                                                              𖠋"
        Mensaje = " "
        tecla = ""



        while win2 == 2:
                time.sleep(.6)
                os.system(c)
                color = random.choice(opciones)
                if color == 10:
                    Robot = "\033[31m" + "                                                                           𖠋"
                    Mensaje = "\033[31m" + "¡Luz Roja!"
                else:
                    Robot = "\033[32m" + "                                                                           𖠋"
                    Mensaje = "\033[32m" + "Jugaremos muévete Luz Verde"

                #Jugador 1

                if len(jugador1) < 78 and estado1 == 1:
                    eleccion1 = random.choice(saltos)
                    jugador1 = eleccion1 + jugador1
                    if eleccion1 != "" and color == 10:
                        estado1 = 2
                elif len(jugador1) < 78 and estado1 == 2:
                    print("Jugador 1 ha sido eliminado")
                    jugador1 = "\033[31m" + jugador1
                elif len(jugador1) > 78 and estado1 == 1:
                    print("Jugador 1 ha pasado")

                #Jugador 2

                if len(jugador2) < 78 and estado2 == 1:
                    eleccion2 = random.choice(saltos)
                    jugador2 = eleccion2 + jugador2
                    if eleccion2 != "" and color == 10:
                        estado2 = 2
                elif len(jugador2) < 78 and estado2 == 2:
                    print("Jugador 2 ha sido eliminado")
                    jugador2 = "\033[31m" + jugador2
                elif len(jugador2) > 78 and estado2 == 1:
                    print("Jugador 2 ha pasado")
                    
                print("\033[0;0m" + "-------------------------------------------------------------------------------")
                print(Mensaje)
                print("                                                                           META")
                print(Robot)
                print("\033[0;0m" + jugador1)
                print("\033[34m" + usuario)
                print("\033[0;0m" + jugador2)
                print("\033[0;0m" + "-------------------------------------------------------------------------------")
                longitud = len(usuario)

                print("Mantenga espacio para avanzar: ")

        
                # Detecta si se presionó la barra espaciadora o el número 1
                if keyboard.is_pressed("space"):
                    tecla = " "  # Barra espaciadora

                #Comprobaciones
                
                #Si la luz es verde y el usuario avanza: funciona
                if tecla == " " and color != 10:
                    usuario = " " + usuario
                    tecla = ""


                #Si la luz es roja y el usuario avanza: funciona
                elif color == 10:
                    time.sleep(1)
                    if keyboard.is_pressed("space"):
                        print("\033[1;31m" + "Has perdido!")
                        puntos = 0
                        print("Perdiste todos tus puntos \n")
                        break
                    else:
                        continue


                if longitud >= 78:
                    print("\033[1;32m" + "Has ganado!")
                    puntos = puntos + 5000
                    print("+5000 \n")
                    time.sleep(3)
                    win2 = 1
    
            
    elif op == 10:
        print ("\nSu puntaje final fue de:",puntos,)
        print ("¡Gracias por jugar!")
        time.sleep(2)
        exit()
    else:
        print("\n Error, opción incorrecta")