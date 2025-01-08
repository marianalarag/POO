class Personaje: 
    #Atributos de la clase
    nombre = "default"
    fuerza = 0
    inteligencia = 0
    vida = 0
    defensa = 0

#Variable de constructor vacío de la clase
mi_personaje = Personaje()
#Modificando los valores a los atributos de la clase
mi_personaje.nombre = "Mariana"
mi_personaje.fuerza = 100
print("El nombre del personaje es: ", mi_personaje.nombre)
print("La fuerza del personaje es: ",mi_personaje.fuerza)

