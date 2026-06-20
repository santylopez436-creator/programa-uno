import random

PALABRAS = [
    "python", "variable", "funcion", "bucle", "clase", "modulo",
    "lista", "diccionario", "cadena", "entero", "ciclo", "programa",
    "algoritmo", "compilador", "interprete", "parametro", "argumento",
    "excepcion", "herencia", "polimorfismo", "recursion", "biblioteca"
]

HORCA = [
    """
  +---+
  |   |
      |
      |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========""",
]

def ahorcado():
    palabra = random.choice(PALABRAS)
    letras_adivinadas = set()
    letras_incorrectas = set()
    max_errores = 6

    print("\n¡Bienvenido al Ahorcado!")
    print("Adivina la palabra letra por letra.\n")

    while True:
        errores = len(letras_incorrectas)
        print(HORCA[errores])

        # Mostrar palabra con guiones
        display = " ".join(c if c in letras_adivinadas else "_" for c in palabra)
        print(f"\nPalabra: {display}")

        if letras_incorrectas:
            print(f"Letras incorrectas: {', '.join(sorted(letras_incorrectas)).upper()}")
        print(f"Errores: {errores}/{max_errores}")

        # Verificar victoria
        if all(c in letras_adivinadas for c in palabra):
            print(f"\n🎉 ¡Ganaste! La palabra era: {palabra.upper()}")
            break

        # Verificar derrota
        if errores >= max_errores:
            print(f"\n💀 ¡Perdiste! La palabra era: {palabra.upper()}")
            break

        # Pedir letra
        letra = input("\nIngresa una letra: ").lower().strip()

        if len(letra) != 1 or not letra.isalpha():
            print("⚠ Por favor ingresa una sola letra válida.")
            continue

        if letra in letras_adivinadas or letra in letras_incorrectas:
            print("⚠ Ya ingresaste esa letra. Intenta con otra.")
            continue

        if letra in palabra:
            letras_adivinadas.add(letra)
            print("✓ ¡Letra correcta!")
        else:
            letras_incorrectas.add(letra)
            print("✗ Letra incorrecta.")

    # Preguntar si jugar de nuevo
    print()
    otra = input("¿Quieres jugar otra vez? (s/n): ").lower().strip()
    if otra == "s":
        ahorcado()
    else:
        print("\n¡Hasta la próxima!\n")


if __name__ == "__main__":
    ahorcado()
