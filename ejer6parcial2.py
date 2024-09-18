class Persona :
    def __init__ ( self , nombre, edad ):
        self.__nombre = nombre 
        self.__edad = edad 
        
    def getdelnombre (self):
        return self.__nombre
    def setnombre (self, nombre ):
        self.__nombre= nombre 
        
    def getedad (self):
        return self.__edad
    def setedad (self, edad ):
        if edad >= 0 :
            self.__edad= edad 
        else :
            print ("la edad no puede ser negativa")
persona = Persona ( "frank", 18)

print  (persona.get__nombre ()) 
print  (persona.get__edad ()) 

persona.set__nombre ("frank ")
persona.set__edad (18)