# ejercicios/ejercicio_4_numero_primo.py
import random

numero = random.randint(1, 100)
es_primo = numero > 1 and all(numero % i != 0 for i in range(2, int(numero**0.5) + 1))

if es_primo:
    print(f"✅ El número {numero} es primo")
else:
    print(f"❌ El número {numero} no es primo")
