#Este programa sirve para saber cuántos horas y minutos se trabajó en una traduccion/revision de un texto.
#Se toma el estimado de palabras por hora y la cantidad de palabras revisadas/traducidas para dar un tiempo estimado

from datetime import datetime

print("\n--------CALCULADORA DE TIEMPO POR PALABRAS---------\n")

while 2>1:
    opcion = input("¿Usar Calculadora? [s/n]: ")

    if opcion == "n":
        print("Has salido.")
        break

    elif opcion == "s":
        words = int(input("Cantidad de palabras por hora: "))
        revised_words = int(input("Palabras traducidas/revisadas: "))
        print("")

        worked = revised_words/words
        worked_hours = int(worked)
        worked_minutes = int((worked - worked_hours)*60)
        if worked_hours == 1 and worked_minutes == 1:
            print("El tiempo trabajado es de {} hora y {} minuto\n".format(worked_hours, worked_minutes))
        elif worked_hours == 1 and worked_minutes != 1:
            print("El tiempo trabajado es de {} hora y {} minutos\n".format(worked_hours, worked_minutes))
        elif worked_hours != 1 and worked_minutes == 1:
            print("El tiempo trabajado es de {} horas y {} minuto\n".format(worked_hours, worked_minutes))
        else:
            print("El tiempo trabajado es de {} horas y {} minutos\n".format(worked_hours, worked_minutes))

    else:
        print("La opción ingresada no es válida.\n")