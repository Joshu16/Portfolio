Numeros = [] #Lista vacia para insertar los 3 numeros
for i in range (3): #epetir 3 veces la pregunta
    num = 1 #Numero inicial para que el while funcione
    while num < 9 or num > 99: #Validacion para que el numero sea de dos digitos utilizando la logica de mayor que nueve y menor que 99 y sino se repita el proceso sin cortar el for
        num = float(input("Ingrese su número de dos digitos: ")) #Solicitacion de numero
        if num < 9 or num > 99: #Comprobacion para dar mensaje de error
            print("Ingrese un número válido.") #Mensaje de error
    Numeros.append(num) #Agregar el numero a la lista
print("El mayor número digitado es:", max(Numeros)) #Print para mostrar el mensaje con el numero mayor utilizando la funcion max
print("El menor número digitado es:", min(Numeros)) #Print para mostrar el mensaje con el numero menor utilizando la funcion min