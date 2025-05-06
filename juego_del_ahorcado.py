

from pickle import TRUE
import random


def obtener_palabra_secreta() -> str:
    palabras = ['mango', 'guayaba', 'mamey', 'guanabana', 'ciruela', 'anon']
    return random.choice(palabras)

def mostrar_avance(palabra_secreta, letras_adivinadas):
    adivinado = ""

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_ "
    return adivinado


def juego_ahorcado():
    palabra_secreta = input("Diga la palabra secreta: ").lower()#obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False

    print("¡Bienvenidos al juego de ahorcad!!")
    print(f"Tienes {intentos} intentos para adivinar")

    print(mostrar_avance(palabra_secreta, letras_adivinadas), "La cantidad deletras de la palabra secreta es: ", len(palabra_secreta))

    while not juego_terminado and intentos > 0:
        adiv = input("Introduce una letra (a-z): ").lower()

        if len (adiv) > 1 or not adiv.isalpha():
            print("Por favor introduzca una letra valida (a-z)")
        elif adiv in letras_adivinadas:
            print("Ya esa letra fue dicha, prueba con otra.")
        else:
            letras_adivinadas.append(adiv)

            if adiv in palabra_secreta:
                print(f"Bien, la letra {adiv} esta presente en la palabra secreta!!!")
                print(mostrar_avance(palabra_secreta, letras_adivinadas))
            else:
                intentos -= 1
                print(f"Lo siento la letra {adiv} no esta presente en la palabra secreta")
                print(f"Te quedan {intentos} intentos.")

        progreso_actual = mostrar_avance(palabra_secreta, letras_adivinadas)

        if "_" not in progreso_actual:
            juego_terminado = TRUE
            print(f"Felicidades has ganado!!! La palabra completa era {palabra_secreta}")
    
    if intentos == 0:
        print(f"Lo siento...Has perdido!!! Se te acabaron los intentos, la palabra era {palabra_secreta}")
juego_ahorcado()