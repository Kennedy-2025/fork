# ejercicios/ejercicio_2_par_impar.py
import random

numero = random.randint(1, 100)
resultado = "par" if numero % 2 == 0 else "impar"
print(f"🔢 El número {numero} es {resultado}")
