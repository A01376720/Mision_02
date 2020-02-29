# Autor: Andy Martínez Hernández, A01376720
# Descripcion: Programa para resolver la distancia que recorre un coche en cierto tiempo, o el tiempo que se tarda en recorrer cierta distancias

# Escribe tu programa después de esta línea.


#Variables

Vel= int (input("Escribe la velocidad del coche en Km/Hr:"))

#Operaciones
Horas1= Vel*6
Horas2= Vel*3.5
distancia= 485/Vel

print ("Si la velocidad del auto es de:", Vel)
print ("La distancia que recorre en 6 hrs es:", Horas1)
print ("La distancia que recorre en 3.5 hrs es de:", Horas2)
print ("Y si viaja 485 km, el tiempo que le toma a esa velocidad es:", distancia)

