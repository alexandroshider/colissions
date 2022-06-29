from matplotlib import pyplot as plt
import random
import particle_object


#Function to change the direction of a particle if it 
#crashes against a right or left wall.
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


#Function to change the direction of a particle if it 
#crashes against a superior or inferior wall.
def bounce_level_wall(wallSize,pos_x,pos_y,vel_x,vel_y):
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

    #particle 1 is a object, it will be the blue point 
    particula1=particle_object.Particle()
    #Initial posicion of blue 
    particula1.posicion(5,3)
    #Initial velocity of blue
    particula1.velocity(random.random(),random.random())
    
    #particle 1 is a object, it will be the red point
    particula2=particle_object.Particle()
    #Initial posicion of red
    particula2.posicion(-2,7)
    #Initial velocity of red
    particula2.velocity(random.random(),random.random())
    
    #This is is how many steps the particles go through
    for i in range(0,150):
        #Plot settings
        a= plt.figure()
        axes= a.add_axes([0.1,0.1,0.8,0.8])
        #Size of the graph
        axes.set_xlim([-10,10])
        axes.set_ylim([-10,10])
        plt.axis('off')

        
        #Conditional for checking if particle bounces with a barrier
        particula1.vel_xaxis=bounce_lateral_wall(wallSize,particula1.pos_xaxis,
            particula1.pos_yaxis,particula1.vel_xaxis,particula1.vel_yaxis)
        particula1.vel_yaxis=bounce_level_wall(wallSize,particula1.pos_xaxis,
            particula1.pos_yaxis,particula1.vel_xaxis,particula1.vel_yaxis)
        #Movement of first particle.
        particula1.pos_xaxis=particula1.pos_xaxis+particula1.vel_xaxis
        particula1.pos_yaxis=particula1.pos_yaxis+particula1.vel_yaxis

        
        #Conditional for checking if particle bounces with a barrier 
        particula2.vel_xaxis=bounce_lateral_wall(wallSize,particula2.pos_xaxis,
            particula2.pos_yaxis,particula2.vel_xaxis,particula2.vel_yaxis)
        particula2.vel_yaxis=bounce_level_wall(wallSize,particula2.pos_xaxis,
            particula2.pos_yaxis,particula2.vel_xaxis,particula2.vel_yaxis)
        #Movement of second particle.
        particula2.pos_xaxis=particula2.pos_xaxis+particula2.vel_xaxis
        particula2.pos_yaxis=particula2.pos_yaxis+particula2.vel_yaxis

        #Put two points in the plot 
        plt.plot(particula1.pos_xaxis,particula1.pos_yaxis,"bo-")
        plt.plot(particula2.pos_xaxis,particula2.pos_yaxis,"ro-")

        #Save the plots as pictures and put a good name so gif is correctly done
        if i<=9:
            plt.savefig(f'line plot00{i}.jpg', bbox_inches='tight', dpi=150)
        if i>=10 and i<=99:
            plt.savefig(f'line plot0{i}.jpg', bbox_inches='tight', dpi=150)
        if i>=100:
            plt.savefig(f'line plot{i}.jpg', bbox_inches='tight', dpi=150)
