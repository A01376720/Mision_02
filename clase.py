# Autor: Andy Martínez Hernández, A01376720
# Descripcion: El programa analiza la cantidad de alumnos inscritos, así como el porcentaje de hombres y mujeres

# Escribe tu programa después de esta línea.

#Variables

Mujeres= int(input("Inserta aquí el número de mujeres inscritas:"))
Hombres= int(input("Inserta aquí el número de hombres inscritos:"))


#Operaciones

TotalA= Mujeres+Hombres
PorM= Mujeres*100//TotalA
PorH= Hombres*100//TotalA

print ("Mujeres inscritas:", Mujeres)
print ("Hombres inscritos:", Hombres)
print ("Total deinscritos:", TotalA)
print ("Porcentaje de mujeres:", PorM, "%")
print ("Procentaje de Hombres:", PorH, "%")
