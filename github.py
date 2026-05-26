#pedro y joseph
#programacion "A"
#calcular descuento dado

# Datos del cliente
precio_original = float(input("Ingresa el precio del producto: "))
color_suerte = input("¿Qué color te tocó? (rojo/amarillo/blanco): ").lower()

# Definir descuento según el color
if color_suerte == "rojo":
    descuento = 40
elif color_suerte == "amarillo":
    descuento = 20
elif color_suerte == "blanco":
    descuento = 0
else:
    print("Color no válido, se aplicará 0% de descuento")
    descuento = 0

# Cálculos
valor_descuento = precio_original * (descuento / 100)
precio_final = precio_original - valor_descuento

# Resultado
print(f"\nDescuento aplicado: {descuento}%")
print(f"Monto del descuento: {valor_descuento:.2f}")
print(f"Total a pagar: {precio_final:.2f}")