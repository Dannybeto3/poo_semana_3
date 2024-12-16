# Función para ingresar las temperaturas diarias
# Esta función solicita al usuario que ingrese la temperatura para cada día de la semana
# y almacena las temperaturas en una lista.

def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
# Esta función toma una lista de temperaturas y calcula el promedio.
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Programa principal
# Esta es la función principal que coordina la entrada de datos y el cálculo del promedio.
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")

# Punto de entrada del programa
# Este bloque asegura que el programa principal se ejecute solo si el script se ejecuta directamente.

if __name__ == "__main__":
    main()

# Definición de la clase ClimaDiario
# Esta clase encapsula la lógica relacionada con la gestión de temperaturas diarias.

class ClimaDiario:
    def __init__(self):
        self.temperaturas = []



    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Programa principal
def main():
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de la temperatura es: {promedio:.2f}")

if __name__ == "__main__":
    main()
