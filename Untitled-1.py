# ejercicios/ejercicio_7_inversor_cadena.py
import random

palabras = ["perro", "universo", "amarillo", "montaña", "python", "ordenador", "nube", "cielo"]
palabra = random.choice(palabras)
invertida = palabra[::-1]

print(f"🔁 Palabra original: {palabra}")
print(f"🔄 Palabra invertida: {invertida}")
