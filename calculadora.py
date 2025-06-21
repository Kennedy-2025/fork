# ejercicios/ejercicio_1_calculadora.py

def calcular(num1, num2, operacion):
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1 - num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "❌ Error: División por cero"
    else:
        return "❌ Operación inválida"

# Puedes cambiar estos valores si lo quieres sin entrada interactiva
num1 = float(input("🧮 Ingresa el primer número: "))
num2 = float(input("🧮 Ingresa el segundo número: "))
operacion = input("🔧 Ingresa la operación (+, -, *, /): ")

resultado = calcular(num1, num2, operacion)
print(f"🧾 Resultado: {num1} {operacion} {num2} = {resultado}")
