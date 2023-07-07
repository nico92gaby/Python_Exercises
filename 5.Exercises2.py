"""
Ejercicio 1: La string mas larga:
Crear una función que reciba una lista de string como entrada y te diga cual es la mas larga de todas
Ej: srtring_mas_larga("hola", "como", "estas")
>estas

def longest_string(string_list = []):
    print(max(string_list))


def main():
    longest_string(["hola", "hola como estas", "tu papa se llama pepe?"])

if __name__ == "__main__":
    main()

Ejercicio 2_ Sumando la lista
Crear una funcion que sume una lista de numeros, no se vale usar la funcion sum
Ej: suma ([1, 2, 3, 4, 5])
>15

def suma(num_list = []):

    suma_op = 0
    for n in num_list:
        suma_op += n
    return print("La suma total de tus numeros es {}".format(suma_op))


def main():
    num_list = []
    b = int(input("Escribe un numero: "))
    num_list.append(b)

    while True:
        c = input("Añadir otro numero? [s/n]: ")
        if c == "n":
            break
        else:

            b = int(input("Escribe un numero: "))
            num_list.append(b)

    suma(num_list)

if __name__ == "__main__":
    main()

Ejercicio 3: Par o impar
Crear una funcion que te de True como resultado si el numero pasado com oargumento es impar.
Ej: es_impar(3)
>True
Es_impar(24)
>False

def impar_detect(n):

    if n % 2 > 0:
        True
        print("True")
    else:
        print("False")

def main():
    impar_detect(192)


if __name__ == "__main__":
    main()

Ejercicio 4: Pregunta algo
Cra una funcion que pregunte al usuario si esta seguro o no, y devuelva los valores "True" o "False" dependiendo
de si el usuario esta seguro o no.

def sure_or_not():
    ans = input("are you sure?[y/n]: ")
    if ans == "y":
        True
        print("True")
    else:
        False
        print("False")


def main():
    sure_or_not()


if __name__ == "__main__":
    main()


Ejercicio 5: A mayus
Crear una funcion que convierta toda una string en mayusculas, no vale usar el metodo upper()

Ejercicio 6: Adivina el número
Crear una funcion que reciba como argumento del 1 al 100 a adivinar y que le pregunte al usuario que adivine el numero.
el codigo se ejecutará hasta que el usuario adivine.

def nostradamus():

    while True:

        win_num = randint(1, 10)

        user_choice = int(input("Adivina en numero del 1  al 10: "))
        if user_choice == win_num:
            print("Acertaste!")
            break
        else:
            print("Has fallado :(")
            print("El numero ganador era: {}".format(win_num))

def main():
    nostradamus()

if __name__ == "__main__":
    main()

Ejercicio 7: Lista de la compra
Crear una funcion que dada una lista de la compra definida fuera de la función,
permita al usuario añadir un nuevo item asegurandose que no exista anteriormente en la lista.

def shop_helper(buy_list = []):
    while True:
        user_choice = input("Qué quieres agregar a la lista de la compra?"
                            "Presiona [q] para salir: ")

        if user_choice == "q":
            print("Esta es tu lista de compra: ")
            for item in buy_list:
                print(item)
            break
        if user_choice not in buy_list:
            buy_list.append(user_choice)
            print("has agregado {} a la lista".format(user_choice))
        else:
            print("ya tienes {} en la lista".format(user_choice))


def main():
    shop_helper(["papas", "huevos", "carne", "leche", "cebollas"])

if __name__ == "__main__":
    main()


"""

