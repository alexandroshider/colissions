
class particle:
    def vel(self, velX, velY):
        self.velInXaxis= velX
        self.velInYaxis= velY
        return self.velInXaxis, self.velInYaxis

    def pos(self, posX, posY):
        self.posInXaxis= posX
        self.posInYaxis= posY
        return self.posInXaxis, self.posInYaxis
        

    