
class Particle:
    def velocity(self, velX, velY):
        self.vel_xaxis= velX
        self.vel_yaxis= velY
        return self.vel_xaxis, self.vel_yaxis

    def posicion(self, posX, posY):
        self.pos_xaxis= posX
        self.pos_yaxis= posY
        return self.pos_xaxis, self.pos_yaxis
        

    