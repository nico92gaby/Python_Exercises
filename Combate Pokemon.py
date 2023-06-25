# COMBATE POKEMON
from random import randint

print("\nBIENVENIDOS AL COMBATE POKEMON\n")

INITIAL_LIFE_PIKA = 90
pikachu_life = INITIAL_LIFE_PIKA

INITIAL_LIFE_SQUI = 95
squirtle_life = INITIAL_LIFE_SQUI

LIFE_LEVEL = 20

ATTACK_OPTIONS  = ["1","2","3"]



while pikachu_life > 0 and squirtle_life > 0:

#----- TURNO PIKACHU

    print("¡Es el turno de Pikachu!\n")

    pikachu_attack = randint(1, 2)

    if pikachu_attack == 1:
        print("Pikachu ha usado Onda Voltio\n")
        squirtle_life -= 20
        if squirtle_life < 0:
            squirtle_life = 0

    else:
        print("Pikachu ha usado Placaje\n")
        squirtle_life -= 15
        if squirtle_life < 0:
            squirtle_life = 0


    life_level_pikachu = int((pikachu_life * LIFE_LEVEL) / INITIAL_LIFE_PIKA)
    life_level_squirtle = int((squirtle_life * LIFE_LEVEL) / INITIAL_LIFE_SQUI)
    print("Vida Squirtle = ({}/{})[{}{}]".format(INITIAL_LIFE_SQUI,
                                                   squirtle_life,
                                                   "#" * life_level_squirtle,
                                                   "-" * (LIFE_LEVEL - life_level_squirtle)))
    print("Vida Pikachu = ({}/{})[{}{}]\n".format(INITIAL_LIFE_PIKA,
                                               pikachu_life,
                                               "#" * life_level_pikachu,
                                               "-" * (LIFE_LEVEL - life_level_pikachu)))
    if squirtle_life == 0:
        print("¡Pikachu ha vencido!")
        break
    else:
        input("Presion Enter para continuar...\n")


#----TURNO SQUIRTLE

    print("¡Ahora es turno de Squirtle!\n")

    squirtle_attack = None

    while squirtle_attack not in ATTACK_OPTIONS:
        squirtle_attack = input("¿Qué ataque deseas usar?\n"
                            "[1]: Placaje\n"
                            "[2]: Pistola de Agua\n"
                            "[3]: Burbuja\n")
        if squirtle_attack == "1":
            print("\n¡Squirle ha usado Placaje!\n")
            pikachu_life -= 60
            if pikachu_life < 0:
                pikachu_life = 0

        elif squirtle_attack == "2":
            print("¡Squirle ha usado Pistola de Agua!\n")
            pikachu_life -= 10
            if pikachu_life < 0:
                pikachu_life = 0

        elif squirtle_attack == "3":
            print("¡Squirle ha usado Burbuja!\n")
            pikachu_life -= 5
            if pikachu_life < 0:
                pikachu_life = 0

        else:
            print("La opción elegida no es correcta\n")



        life_level_pikachu = int((pikachu_life * LIFE_LEVEL) / INITIAL_LIFE_PIKA)
        life_level_squirtle = int((squirtle_life * LIFE_LEVEL) / INITIAL_LIFE_SQUI)
        print("Vida Squirtle = ({}/{})[{}{}]".format(INITIAL_LIFE_SQUI,
                                               squirtle_life,
                                               "#" * life_level_squirtle,
                                               "-" * (LIFE_LEVEL - life_level_squirtle)))
        print("Vida Pikachu = ({}/{})[{}{}]\n".format(INITIAL_LIFE_PIKA,
                                               pikachu_life,
                                               "#" * life_level_pikachu,
                                               "-" * (LIFE_LEVEL - life_level_pikachu)))

        if pikachu_life == 0:
            print("¡Squirtle ha vencido!")
        else:
            input("Presion Enter para continuar...\n")


