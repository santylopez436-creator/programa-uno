import random

# ── Categorías de palabras ────────────────────────────────────────────────────
CATEGORIAS = {
    "1": {
        "nombre": "Animales",
        "palabras": [
            "elefante", "jirafа", "cocodrilo", "mariposa", "tigre",
            "delfin", "camello", "gorila", "serpiente", "aguila",
            "tortuga", "hipopotamo", "leopardo", "pingüino", "rinoceronte",
            "flamenco", "canguro", "puercoespin", "murciélago", "medusa",
            "caballo", "lobo", "zorro", "ballena", "pantera"
        ]
    },
    "2": {
        "nombre": "Cosas",
        "palabras": [
            "silla", "ventana", "paraguas", "mochila", "televisor",
            "escalera", "calendario", "espejo", "cuchara", "linterna",
            "boligrafo", "alfombra", "maletín", "lámpara", "reloj",
            "paraguas", "tijeras", "termómetro", "botella", "teléfono",
            "computadora", "impresora", "cuaderno", "calculadora", "estante"
        ]
    },
    "3": {
        "nombre": "Frutas",
        "palabras": [
            "manzana", "naranja", "fresas", "platano", "sandia",
            "mango", "papaya", "piña", "cereza", "durazno",
            "mandarina", "uva", "pera", "kiwi", "melon",
            "maracuyá", "guayaba", "higo", "ciruela", "coco",
            "frambuesa", "granada", "limon", "aguacate", "mora"
        ]
    },
    "4": {
        "nombre": "Países",
        "palabras": [
            "colombia", "argentina", "brasil", "mexico", "peru",
            "venezuela", "chile", "ecuador", "bolivia", "paraguay",
            "uruguay", "cuba", "panama", "honduras", "guatemala",
            "nicaragua", "costarica", "españa", "portugal", "francia",
            "alemania", "italia", "japon", "china", "australia"
        ]
    },
    "5": {
        "nombre": "Deportes",
        "palabras": [
            "futbol", "baloncesto", "natacion", "tenis", "voleibol",
            "ciclismo", "atletismo", "boxeo", "judo", "esgrima",
            "gimnasia", "remo", "equitacion", "arqueria", "esqui",
            "surfing", "escalada", "triatlón", "béisbol", "rugby",
            "polo", "karate", "taekwondo", "badminton", "handball"
        ]
    },
    "6": {
        "nombre": "Nombres de personas",
        "palabras": [
            "alejandro", "valentina", "sebastian", "camila", "mateo",
            "isabella", "daniel", "sofia", "nicolas", "gabriela",
            "andres", "mariana", "santiago", "paula", "felipe",
            "catalina", "juan", "natalia", "carlos", "andrea",
            "roberto", "patricia", "miguel", "diana", "fernando"
        ]
    },
    "7": {
        "nombre": "Programación",
        "palabras": [
            "variable", "funcion", "bucle", "clase", "modulo",
            "lista", "diccionario", "cadena", "entero", "algoritmo",
            "compilador", "interprete", "parametro", "excepcion", "herencia",
            "polimorfismo", "recursion", "biblioteca", "depuracion", "sintaxis",
            "operador", "condicion", "iteracion", "puntero", "interfaz"
        ]
    },
}

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
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========""",
]


def mostrar_menu_categorias():
    print("\n" + "=" * 40)
    print("       ELIGE UNA CATEGORÍA")
    print("=" * 40)
    for clave, info in CATEGORIAS.items():
        print(f"  [{clave}] {info['nombre']}")
    print("=" * 40)


def elegir_categoria():
    while True:
        mostrar_menu_categorias()
        opcion = input("Ingresa el número de categoría: ").strip()
        if opcion in CATEGORIAS:
            categoria = CATEGORIAS[opcion]
            print(f"\n✔ Categoría seleccionada: {categoria['nombre']}\n")
            return categoria
        else:
            print("⚠ Opción no válida. Por favor elige un número del 1 al 7.")


def ahorcado(nombre):
    # Elegir categoría
    categoria = elegir_categoria()
    palabra = random.choice(categoria["palabras"])
    letras_adivinadas = set()
    letras_incorrectas = set()
    max_errores = 6

    print(f"¡Buena suerte, {nombre}! Adivina la palabra de la categoría '{categoria['nombre']}'.\n")

    while True:
        errores = len(letras_incorrectas)
        print(HORCA[errores])

        # Mostrar categoría y palabra con guiones
        print(f"  Categoría : {categoria['nombre']}")
        display = " ".join(c if c in letras_adivinadas else "_" for c in palabra)
        print(f"  Palabra   : {display}  ({len(palabra)} letras)")

        if letras_incorrectas:
            print(f"  Incorrectas: {', '.join(sorted(letras_incorrectas)).upper()}")
        print(f"  Errores   : {errores}/{max_errores}")

        # Verificar victoria
        if all(c in letras_adivinadas for c in palabra):
            print(f"\n{'=' * 40}")
            print(f"  🎉 ¡FELICITACIONES, {nombre.upper()}!")
            print(f"  ¡Ganaste! La palabra era: {palabra.upper()}")
            print(f"  Categoría: {categoria['nombre']}")
            print(f"{'=' * 40}\n")
            break

        # Verificar derrota
        if errores >= max_errores:
            print(f"\n{'=' * 40}")
            print(f"  💀 ¡LO SIENTO, {nombre.upper()}!")
            print(f"  Perdiste. La palabra era: {palabra.upper()}")
            print(f"  Categoría: {categoria['nombre']}")
            print(f"{'=' * 40}\n")
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
    otra = input("¿Quieres jugar otra vez? (s/n): ").lower().strip()
    if otra == "s":
        ahorcado(nombre)
    else:
        print(f"\n¡Hasta la próxima, {nombre}!\n")


if __name__ == "__main__":
    print("\n" + "=" * 40)
    print("       JUEGO DEL AHORCADO")
    print("=" * 40)
    nombre = input("Ingresa tu nombre: ").strip()
    while not nombre:
        nombre = input("El nombre no puede estar vacío. Ingresa tu nombre: ").strip()
    print(f"\n¡Hola, {nombre}! Bienvenido al Ahorcado.")
    ahorcado(nombre)
