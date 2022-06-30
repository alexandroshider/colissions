from matplotlib import pyplot as plt
import random
import particle_object

"""
Functions to change the direction of a particle if it 
crashes against a right or left wall and upper or lower wall. 
Args are:
-size of the box/2
-positions in x and y axes
-velocities in x and y axes
"""
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
    #This is the number of particles in square box
    number_of_particles=int(20)
    #This is the number of steps each particle will cover
    steps=200
    #Dimension is 
    box_lenght_side=10
    #Speed is for speed up the particles
    speed=1
    #wallSize is the size of the box where particles bounce
    wallSize=box_lenght_side/2

    """
    In this loop I create the instances (particles) and save
    them in a list.
    Also, we call position and velocity methods in this loop
    so each instance have initial position and initial velocity.
    """
    particulas=[]
    for i in range(0,number_of_particles):
        #particulas_object=particle_object.Particle()
        particulas.append(particle_object.Particle())
        #particle's atributes are defined
        particulas[i].posicion(random.randint(-int(wallSize)+1,
            int(wallSize)-1),random.randint(-int(wallSize)+1,int(wallSize)-1))
        #Initial velocity of blue
        particulas[i].velocity(random.uniform(-int(wallSize)/10*speed,
            int(wallSize)/10*speed),random.uniform(-int(wallSize)/10*speed, 
            int(wallSize)/10*speed))
    #This is is how many steps the particles go through
    for j in range(0,int(steps)):
        #Plot settings
        a= plt.figure()
        axes= a.add_axes([0.1,0.1,0.8,0.8])
        #Size of the square
        axes.set_xlim([-wallSize,wallSize])
        axes.set_ylim([-wallSize,wallSize])
        plt.axis('off')
        for i in range(0,number_of_particles):
            #Conditional for checking if particle bounces with a barrier
            #Then this functions return the velocity of the i-th particle. 
            particulas[i].vel_xaxis=bounce_lateral_wall(wallSize,particulas[i].pos_xaxis,
                particulas[i].pos_yaxis,particulas[i].vel_xaxis,particulas[i].vel_yaxis)
            particulas[i].vel_yaxis=bounce_level_wall(wallSize,particulas[i].pos_xaxis,
                particulas[i].pos_yaxis,particulas[i].vel_xaxis,particulas[i].vel_yaxis)
            #Movement of first particle. This is like
            #Final position = initial position + step in each axis
            particulas[i].pos_xaxis=particulas[i].pos_xaxis+particulas[i].vel_xaxis
            particulas[i].pos_yaxis=particulas[i].pos_yaxis+particulas[i].vel_yaxis
            #Draw the i-th point on the plot 
            plt.plot(particulas[i].pos_xaxis,particulas[i].pos_yaxis,"bo-")
        
        #Save the plots as pictures and put a good name so gif is correctly done
        if j<=9:
            plt.savefig(f'line plot00{j}.jpg', bbox_inches='tight', dpi=150)
        if j>=10 and j<=99:
            plt.savefig(f'line plot0{j}.jpg', bbox_inches='tight', dpi=150)
        if j>=100:
            plt.savefig(f'line plot{j}.jpg', bbox_inches='tight', dpi=150)
