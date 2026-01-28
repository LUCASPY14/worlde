import random

PALABRAS = [
    "perro", "gatos", "silla", "mesa", "carta",
    "nubes", "pluma", "llave", "fuego", "piano"
]

PALABRA_SECRETA = random.choice(PALABRAS)
INTENTOS_MAX = 6

print("🎮 WORDLE en Python")
print("Adivina la palabra de 5 letras")
print("🟩 correcta y bien colocada | 🟨 correcta pero mal colocada | ⬜ incorrecta")

intentos = 0

while intentos < INTENTOS_MAX:
    intento = input(f"\nIntento {intentos + 1}/{INTENTOS_MAX}: ").lower()

    if len(intento) != 5:
        print("❌ La palabra debe tener 5 letras")
        continue

    resultado = ["⬜"] * 5
    palabra_temp = list(PALABRA_SECRETA)

    # Letras correctas y bien colocadas
    for i in range(5):
        if intento[i] == PALABRA_SECRETA[i]:
            resultado[i] = "🟩"
            palabra_temp[i] = None

    # Letras correctas pero mal colocadas
    for i in range(5):
        if resultado[i] == "⬜" and intento[i] in palabra_temp:
            resultado[i] = "🟨"
            palabra_temp[palabra_temp.index(intento[i])] = None

    print(" ".join(resultado))

    if intento == PALABRA_SECRETA:
        print("🎉 ¡Ganaste!")
        break

    intentos += 1

if intentos == INTENTOS_MAX and intento != PALABRA_SECRETA:
    print(f"😢 Perdiste. La palabra era: {PALABRA_SECRETA}")
