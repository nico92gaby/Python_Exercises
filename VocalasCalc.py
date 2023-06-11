#ESTE PROGRAMA ES UN CONTADOR DE VOCALES



#PARAMETROS Y VARIABLES
vocales = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "ü"]


#CODIGO
print("------------CONTADOR DE VOCALES-------------\n")

texto = None

while texto != "q":
    resultado = 0
    vocales_usadas = []
    texto = input("Escriba o pegue un texto y para saber la cantidad de vocales usadas. Indique [q] para salir: \n"
                  "")
    if texto == "q":
        print("Ha seleccionado salir")
        break
    else:
        for letra in texto:

            if letra in vocales:
                resultado += 1
                vocales_usadas.append(letra)
            else:
                print("No hay vocales en este texto.")
        print("La cantidad de vocales presentes en el texto son: {}".format(resultado))
        print("Las vocales usadas fueron: {}\n".format(vocales_usadas))













