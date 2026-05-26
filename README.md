#pedro y josehp
#pragramacion 2 "A"
#codigo de colcular el descuanto dado

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

    
