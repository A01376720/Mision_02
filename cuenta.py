# Autor: Andy Martínez Hernández
# Descripcion: El programa saca el precio de la comida, sacando IVA, propina, y Subtotal. Y usándolos para sacar el precio total de la comida

# Escribe tu programa después de esta línea.

#Variables

Subtotal= int (input("Escribe aquí el precio de tu comida:"))

#Operaciones

IVA= Subtotal*0.16
Propina= Subtotal*0.13
Totalpago= Subtotal+IVA+Propina

print ("El subtotal de tu comida es:", Subtotal)
print ("El IVA es de:", IVA)
print ("La propina es de:", Propina)
print ("y por ende, el precio completo real de tu familia sería de:", Totalpago)
