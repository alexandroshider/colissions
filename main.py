from matplotlib import pyplot as plt
import random

if __name__ == "__main__":
    #wallSize is the size of the box
    wallSize=10


    

    #Posición inicial
    R0=[0,0]
    #grafica del primer punto
    plt.plot([R0[0]],[R0[1]],"ro-")



    #x and y are the positions in x-axis and y-axis
    #These are the initial positions
    posX=5
    posY=3
    print(0,posX,posY)
    #velX and velY are the initial step in each axis. These is 
    #random. 
    velX=random.random()
    velY=random.random()
    #velX=0.838921681345721 #random.random()
    #velY=0.186587084087627 #random.random()
    #The particle gives 100 steps
    for i in range(0,100):
        #Particle moves in x and y
        #Configuración de los ejes de la caminata
        a= plt.figure()
        axes= a.add_axes([0.1,0.1,0.8,0.8])
        # adding axes
        axes.set_xlim([-10,10])
        axes.set_ylim([-10,10])
        posX=posX+velX
        posY=posY+velY

        if posX>wallSize or posX<-wallSize:
            slope=(posY-(posY-velY))/(posX-(posX-velX))            
            if posX<-wallSize:
                posY=-slope*wallSize-slope*posX+posY
                posX=-wallSize
            if posX>wallSize:
                posY=slope*wallSize-slope*posX+posY
                posX=wallSize
            velX=-velX

        if posY>wallSize or posY<-wallSize:
            slope=(posY-(posY-velY))/(posX-(posX-velX))
            
            if posY<-wallSize:
                posX=-wallSize/slope-posY/slope+posX
                posY=-wallSize
            if posY>wallSize:
                posX=wallSize/slope-posY/slope+posX
                posY=wallSize
            velY=-velY
        print(i+1,posX,posY)
        plt.plot(posX,posY,"bo-")
        if i<=9:
            plt.savefig(f'line plot0{i}.jpg', bbox_inches='tight', dpi=150)
        if i>=10:
            plt.savefig(f'line plot{i}.jpg', bbox_inches='tight', dpi=150)
        
        
