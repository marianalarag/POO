class Personaje: 

    def __init__(self,nombre,fuerza,inteligencia,vida,defensa):
        self.__nombre = nombre #el signo de igual es de asignación
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__vida = vida
        self.__defensa = defensa

    def atributos (self):
        print(f"-Nombre: {self.__nombre}\n-Fuerza: {self.__fuerza}\n-Inteligencia: {self.__inteligencia}\n-Vida: {self.__vida}\n-Defensa: {self.__defensa}")
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.__fuerza += fuerza #Ya a la variable de self.__fuerza, se le va a agregar la fuerza que defina el usuario en fuerza
        self.__fuerza = self.__fuerza + fuerza
        self__inteligencia = self__inteligencia + inteligencia
        self__defensa = self__defensa + defensa
    
    def esta_vivo(self):
        return self.__vida > 0 
    
    def morir(self):
        self.__vida = 0
        print(f"{self.__nombre} ha muerto")
    
    def dañar(self,enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza > enemigo.__defensa else 0
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida -= daño
        print(f"{self.__nombre} ha realizado {daño} puntos de daño a {enemigo.__nombre}")
        if not enemigo.esta_vivo():
            enemigo.morir()
        print(f"Vida de {enemigo.__nombre} es {enemigo.__vida}")
    
    #Obtener el valor
    def get_fuerza(self):
        return self.__fuerza
    
    #Cambiar valor
    def set_fuerza(self,fuerza):
        if fuerza < 0:
            print("ERROR, has puesto un valor negativo")
        else:
            self.__fuerza = fuerza

#Variable de constructor vacío de la clase
mi_personaje = Personaje("Trakalosa de Monterrey",70,90,100,50)
mi_enemigo = Personaje("La arrolladora banda limón",60,90,100,40)
#Prueba 4
mi_personaje.atacar(mi_enemigo)
#Prueba 7. Getters and setters
mi_personaje._Personaje__fuerza = 10
print(mi_personaje.get_fuerza())







