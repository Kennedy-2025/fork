# ejercicios/ejercicio_3_vocales.py
import random

palabras = [
    "Aceituna", "Murciélago", "Educación", "Aeropuerto", "Otorrinolaringólogo",
    "Euforia", "Aceite", "Paleontólogo", "Arquitectura", "Hipopótamo"
]

vocales = "AEIOUÁÉÍÓÚaeiouáéíóú"
palabra = random.choice(palabras)
encontradas = [letra for letra in palabra if letra in vocales]

print(f"📝 Palabra seleccionada: {palabra}")
print(f"🔤 Vocales encontradas: {', '.join(encontradas)}")
print(f"🔢 Total de vocales: {len(encontradas)}")
