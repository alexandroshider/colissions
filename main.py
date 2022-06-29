from matplotlib import pyplot as plt
import random
import particle_object

def bounce_lateral_wall(wallSize,pos_x,pos_y,vel_x,vel_y):
    
    if pos_x>wallSize or pos_x<-wallSize:
        slope=(pos_y-(pos_y-vel_y))/(pos_x-(pos_x-vel_x))            
        if pos_x<-wallSize:
            pos_y=-slope*wallSize-slope*pos_x+pos_y
            pos_x=-wallSize
        if pos_x>wallSize:
            pos_y=slope*wallSize-slope*pos_x+pos_y
            pos_x=wallSize
        vel_x=-vel_x
    return vel_x

def bounce_level_wall(wallSize,pos_x,pos_y,vel_x,vel_y):
    #print(pos_y,vel_y)
    if pos_y>wallSize or pos_y<-wallSize:
        slope=(pos_y-(pos_y-vel_y))/(pos_x-(pos_x-vel_x))
        if pos_y<-wallSize:
            pos_x=-wallSize/slope-pos_y/slope+pos_x
            pos_y=-wallSize
        if pos_y>wallSize:
            pos_x=wallSize/slope-pos_y/slope+pos_x
            pos_y=wallSize
        vel_y=-vel_y
    return vel_y



if __name__ == "__main__":
    #wallSize is the size of the box where particles bounce
    wallSize=10

    
    #x and y are the positions in x-axis and y-axis
    #These are the initial positions of a particle
    particula1=particle_object.Particle()
    particula1.posicion(5,3)
    particula1.velocity(0.41,0.67)
    
    particula2=particle_object.Particle()
    particula2.posicion(-2,7)
    particula2.velocity(0.53,-0.32)
    
    """ Second particle. Implementation not yet.
    particula2=particle_object.Particle()
    particula2.posicion(-4,-2)
    particula2.velocity(random.random(),random.random())
    pos_x=particula1.pos_xaxis
    pos_y=particula1.pos_yaxis
    #velX and velY are the initial step in each axis. These is 
    #random. 
    vel_x=particula1.vel_xaxis
    vel_y=particula1.vel_yaxis
    """
    #velX=0.838921681345721 #random.random()
    #I tried to make for two particles, It would be more complicated
    #velY=0.186587084087627 #random.random()
    #The particle gives 100 steps
    for i in range(0,150):
        #Particle moves in x and y
        #Configuración de los ejes de la caminata
        a= plt.figure()
        axes= a.add_axes([0.1,0.1,0.8,0.8])
        # adding axes
        axes.set_xlim([-10,10])
        axes.set_ylim([-10,10])
        plt.axis('off')
        """
        pos_x=particula1.pos_xaxis
        pos_y=particula1.pos_yaxis
        #velX and velY are the initial step in each axis. These is 
        #random. 
        vel_x=particula1.vel_xaxis
        vel_y=particula1.vel_yaxis
        
        hay que cambiar estas pos_X a pos_xaxis
        y lo mismo para el caso del y
        Y hacelo para ambas particulas
        De esta forma todo se queda estático, siempre se 
        redeclara en las posiciones inciales, ya que el atributo
        de cada instancia no cambia. 
        
        tal vez es necesario hacerlo todo dentro de un loop
        para más partículas

        """
        #vel_x=particula1.vel_xaxis
        #vel_y=particula1.vel_yaxis        
        #pos_x=particula1.pos_xaxis+vel_x
        #pos_y=particula1.pos_yaxis+vel_y
        #I put the conditional in a method in order to reduce space
        particula1.vel_xaxis=bounce_lateral_wall(wallSize,particula1.pos_xaxis,particula1.pos_yaxis,particula1.vel_xaxis,particula1.vel_yaxis)
        particula1.vel_yaxis=bounce_level_wall(wallSize,particula1.pos_xaxis,particula1.pos_yaxis,particula1.vel_xaxis,particula1.vel_yaxis)
        particula1.pos_xaxis=particula1.pos_xaxis+particula1.vel_xaxis
        particula1.pos_yaxis=particula1.pos_yaxis+particula1.vel_yaxis

        particula2.vel_xaxis=bounce_lateral_wall(wallSize,particula2.pos_xaxis,particula2.pos_yaxis,particula2.vel_xaxis,particula2.vel_yaxis)
        particula2.vel_yaxis=bounce_level_wall(wallSize,particula2.pos_xaxis,particula2.pos_yaxis,particula2.vel_xaxis,particula2.vel_yaxis)
        particula2.pos_xaxis=particula2.pos_xaxis+particula2.vel_xaxis
        particula2.pos_yaxis=particula2.pos_yaxis+particula2.vel_yaxis

        #This conditional makes ball bounce in the superior and inferior faces

            
        #print(i+1,posX,posY)
        plt.plot(particula1.pos_xaxis,particula1.pos_yaxis,"bo-")
        plt.plot(particula2.pos_xaxis,particula2.pos_yaxis,"ro-")
        """
        particula1.pos_xaxis=pos_x
        particula1.pos_yaxis=pos_y
        
        vel_x=particula2.vel_xaxis
        vel_y=particula2.vel_yaxis        
        pos_x=particula2.pos_xaxis+vel_x
        pos_y=particula2.pos_yaxis+vel_y

        if pos_x>wallSize or pos_x<-wallSize:
            slope=(pos_y-(pos_y-vel_y))/(pos_x-(pos_x-vel_x))            
            if pos_x<-wallSize:
                pos_y=-slope*wallSize-slope*pos_x+pos_y
                pos_x=-wallSize
            if pos_x>wallSize:
                pos_y=slope*wallSize-slope*pos_x+pos_y
                pos_x=wallSize
            particula1.vel_xaxis=-vel_x
            
        #This conditional makes ball bounce in the superior and inferior faces
        if pos_y>wallSize or pos_y<-wallSize:
            slope=(pos_y-(pos_y-vel_y))/(pos_x-(pos_x-vel_x))
            if pos_y<-wallSize:
                pos_x=-wallSize/slope-pos_y/slope+pos_x
                pos_y=-wallSize
            if pos_y>wallSize:
                pos_x=wallSize/slope-pos_y/slope+pos_x
                pos_y=wallSize
            particula1.vel_yaxis=-vel_y
            
        #print(i+1,posX,posY)
        particula2.pos_xaxis=pos_x
        particula2.pos_yaxis=pos_y
        plt.plot(pos_x,pos_y,"ro-")
        """
        """
        pos_x=particula2.pos_xaxis
        pos_y=particula2.pos_yaxis
        #velX and velY are the initial step in each axis. These is 
        #random. 
        vel_x=particula2.vel_xaxis
        vel_y=particula2.vel_yaxis
        pos_x=pos_x+vel_x
        pos_y=pos_y+vel_y

        if pos_x>wallSize or pos_y<-wallSize:
            slope=(pos_y-(pos_y-vel_y))/(pos_x-(pos_x-vel_x))            
            if pos_x<-wallSize:
                pos_y=-slope*wallSize-slope*pos_x+pos_y
                pos_x=-wallSize
            if pos_x>wallSize:
                pos_y=slope*wallSize-slope*pos_x+pos_y
                pos_x=wallSize
            vel_x=-vel_x

        if pos_y>wallSize or pos_y<-wallSize:
            slope=(pos_y-(pos_y-vel_y))/(pos_x-(pos_x-vel_x))
            
            if pos_y<-wallSize:
                pos_x=-wallSize/slope-pos_y/slope+pos_x
                pos_y=-wallSize
            if pos_y>wallSize:
                pos_x=wallSize/slope-pos_y/slope+pos_x
                pos_y=wallSize
            vel_y=-vel_y
        #print(i+1,posX,posY)
        plt.plot(pos_x,pos_y,"ro-")
        """
        if i<=9:
            plt.savefig(f'line plot00{i}.jpg', bbox_inches='tight', dpi=150)
        if i>=10 and i<=99:
            plt.savefig(f'line plot0{i}.jpg', bbox_inches='tight', dpi=150)
        if i>=100:
            plt.savefig(f'line plot{i}.jpg', bbox_inches='tight', dpi=150)
