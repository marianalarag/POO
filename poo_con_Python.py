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
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa
    
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

class Guerrero(Personaje):
    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa,espada = 0):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)  # Se pasa solo lo necesario a la clase base
        self.espada = espada  # Se asigna el atributo específico de Guerrero
    
    #Pedirle al usuario escoger un arma
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Espada de plata, daño 10. (2) Espada de bronce, daño 8\n"))
        if opcion == 1:
            self.espada == 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Valor incorrecto")

    #Sobreescribir método
    def atributos(self):
        super().atributos()
        print(f"-Espada: {self.espada}")
    
    #Sonrescribir el cálclulo de daño
    def dañar (self,enemigo):
        return self.fuerza*self.espada - enemigo.defensa

class Mago(Personaje):
    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, vida, defensa,libro = 0):
        super().__init__(nombre, fuerza, inteligencia, vida, defensa)  # Se pasa solo lo necesario a la clase base
        self.libro = libro  # Se asigna el atributo específico de Guerrero

    #Sobreescribir método
    def atributos(self):
        super().atributos()
        print(f"-Libro: {self.libro}")
    
    #Sonrescribir el cálclulo de daño
    def dañar (self,enemigo):
        return self.inteligencia*self.libro - enemigo.defensa

trakalosa = Personaje("Trakalosa de Monterrey", 20,15,10,100)
hercules = Guerrero("Hércules", 20, 15, 10, 100,5)
dios = Mago("Dios",20,15,10,100,5)
#Imprimir atributos
hercules.atributos()
trakalosa.atributos()
dios.atributos()

#Ataques
trakalosa.atacar(hercules)
hercules.atacar(dios)
dios.atacar(trakalosa)

#Imprimir atributos
hercules.atributos()
trakalosa.atributos()
dios.atributos()

#Variable de constructor vacío de la clase
mi_personaje = Personaje("Trakalosa de Monterrey",70,90,100,50)
mi_enemigo = Personaje("La arrolladora banda limón",60,90,100,40)
#Prueba 4
mi_personaje.atacar(mi_enemigo)
#Prueba 7. Getters and setters
mi_personaje._Personaje__fuerza = 10
print(mi_personaje.get_fuerza())







