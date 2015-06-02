import random

class Sardina(object):
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.z = random.randint(0, 1000)
        self.hp = 1

    def hp(self):
        hp = self.hp
        return hp
        
    def __str__(self):
        return "{},{},{}".format(self.x, self.y, self.z)

    def posx(self):
        x = self.x
        return x
    
    def posy(self):
        y = self.y
        return y
    
    def posz(self):
        z = self.z
        return z
    
    def mover(self):
        self.x += random.randint(-100,100)
        self.y += random.randint(-100,100)
        self.z += random.randint(-100,100)
    def mover2(self):
        self.x += random.randint(-3,3)
        self.y += random.randint(-3,3)
        self.z += random.randint(-3,3)
        
sardina1 = Sardina()

class Jugador():
    def atacar(self,a,b,c):
            if  int(a) == sardina1.posx() and int(b) == sardina1.posy() and int(c) == sardina1.posz():
                print(a,b,c)
                sardina1.hp -= 1
            if sardina1.hp == 0:
                print("Disparo acertado " + "\n Objetivo destruido en: "+
                  "{},{},{}".format(sardina1.posx(),sardina1.posy(),sardina1.posz()))
            elif sardina1.hp == 1:
                print("Disparo fallido")
                sardina1.mover()
player = Jugador()            
print("Un banco de sardinas geneticamente modificadas"
    +"\n para asesinar a pescadores ha escapado"
    +"\n y tu deber ahora es eliminarlas, puedes hacer uso de tus"
    +"\n cohetes submarinos para destruirles antes que puedan"
    +"destruir la industria nacional")
print("Para saber su posicion puedes usar tu radar, "
      +"\n escribiendo 'radar'(el radar tiene una incertudumbre de 3,"+
      "\nuna vez conozcas su posicon puedes atacar escribiendo 'atacar'")¡

class turnos(object):
    def iniciar(self):    
        while sardina1.hp == 1:
            ini = input("Que deseas hacer? ")
            if __name__ == '__main__':
                if ini.lower() == "atacar":
                    a,b,c = input("ingrese coordenadas x,y,z: " ).split(",")
                    player.atacar(a,b,c)
                elif ini.lower() == "radar":
                    print(sardina1.__str__())
                    sardina1.mover2()
                else:
                    print("no es una opcion")
                    
                    
play = turnos()                   
if __name__== '__main__':
    play.iniciar()
                
    








