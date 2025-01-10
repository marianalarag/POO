class Personaje: 

    def __init__(self,nombre,fuerza,inteligencia,vida,defensa):
        self.nombre = nombre #el signo de igual es de asignación
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.vida = vida
        self.defensa = defensa

    def atributos (self):
        print(f"-Nombre: {self.nombre}\n-Fuerza: {self.fuerza}\n-Inteligencia: {self.inteligencia}\n-Vida: {self.vida}\n-Defensa: {self.defensa}")
    
    def subir_nivel(self,fuerza,inteligencia,defensa):
        self.fuerza += fuerza #Ya a la variable de self.fuerza, se le va a agregar la fuerza que defina el usuario en fuerza
        self.fuerza = self.fuerza + fuerza
    
    def esta_vivo(self):
        return self.vida > 0 
    
    def morir(self):
        self.vida = 0
        print(f"ha muerto {self.nombre}")
    
    def dañar(self,enemigo):
        return self.fuerza - enemigo.defensa
    
    def atacar(self,enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        print(f"Vida de {enemigo.nombre} es {enemigo.vida}")



#Variable de constructor vacío de la clase
mi_personaje = Personaje("trakalosa de monterrey",70,90,100,50)
mi_enemigo = Personaje("La arrolladora banda limón",60,90,100,40)
print(mi_personaje.dañar(mi_enemigo))
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos






