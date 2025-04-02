import random

random.seed()

# 0107882854
def generar_verificador(cedula_sin_verificador):
    suma_impar = 0
    for i in range(0, 9, 2):
        multiplicacion = int(cedula_sin_verificador[i]) * 2
        suma_impar += multiplicacion if multiplicacion <= 9 else multiplicacion - 9
    suma_par = sum(map(int, cedula_sin_verificador[1::2]))
    resultado = 10 - ((suma_impar + suma_par) % 10)
    return resultado if resultado < 10 else 0

# Pedir cantidad de cédulas a generar
cantidad = int(input("¿Cuántas cédulas desea generar? "))

# Generar cédulas válidas
for i in range(cantidad):
    # Generar provincia, tercer dígito y secuencial
    provincia = str(random.randint(1, 24)).zfill(2)
    tercer_digito = str(random.randint(0, 5))
    secuencial = str(random.randint(1, 999999)).zfill(6)
    cedula_sin_verificador = provincia + tercer_digito + secuencial

    # Generar verificador
    verificador = generar_verificador(cedula_sin_verificador)

    # Mostrar cédula generada
    cedula = cedula_sin_verificador + str(verificador)
    print(cedula)
    
