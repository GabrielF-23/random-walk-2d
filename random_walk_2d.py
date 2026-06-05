import numpy as np
import matplotlib.pyplot as plt 
import random as random

def rw_2d(n):
    '''Caminhante Aleatorio em 2D, onde 'n' = número de passos - 
       Random Walk 2D, where 'n' = number of steps'''

        #Origem em x = 0
    #Origin at x = 0
    x = 0
    y = 0
    a = [0]
    b = [0]

    #Condição do caminhante aleatorio em 2D 25% direita, 25% cima, 25% esquerda e 25% baixo.
    #Random Walk 2D condition 25% right, 25% top, 25% left and 25% bottom.
    for i in range(n):
        step = random.choice([1,2,3,4])

        if step == 1:
            x += 1
        elif step == 2:
            x -= 1
        elif step == 3:
            y += 1
        else:
            y -= 1

        a.append(x)
        b.append(y)

    return a,b

#Rodadas
#Runs.
r = 1000

#Passos.
#Steps.
s = 1000

#Lista de caminhadas.
#Walk list.
walk = []

#For que gera varios caminhantes da origem.
#Loop that create multiple walkers from the origin.
for i in range(r):
    walk.append(rw_2d(s))

#Gera o subplot.
#Generate the subplot.
fig, axs = plt.subplots(2,2, figsize=(12,10), dpi=100, constrained_layout=True)

#Lista de pontos finais das trajetórias em x e y.
#Endpoints of the trajectories list at x and y.
endp_x = []
endp_y = []

#Percorre a lista 'walk' e cria lista de todos os pontos finais das trajetórias.
#Iterates through the 'walk' list and creates a list of all the endpoints of the trajectories.
for a,b in walk:
    axs[0,0].plot(a,b, alpha=0.8)

    endp_x.append(a[-1])
    endp_y.append(b[-1])

#Gráfico das trajetórias dos caminhantes.
#Random walk trajectories graph.
axs[0,0].set_title(f"Trajetória dos caminhantes. {s} passos - {r} runs")
axs[0,0].set_xlabel("X")
axs[0,0].set_ylabel("Y")
axs[0,0].grid()

#Gŕafico de disperção das posições finais.
#Final position dispersion graph.
axs[0,1].scatter(endp_x, endp_y)
axs[0,1].set_title(f"Disperção das posições finais. {s} passos - {r} runs")
axs[0,1].set_xlabel("X")
axs[0,1].set_ylabel("Y")
axs[0,1].grid()

#Histograma das posições finais em x.
#Histogram of final positions at x.
axs[1,0].hist(endp_x, bins=30)
axs[1,0].set_title(f"Histograma de posições finais em x. {s} passos - {r} runs")
axs[1,0].set_xlabel("Posição final em x")
axs[1,0].set_ylabel("Frequência")
axs[1,0].grid()

#Histograma das posições finais em y.
#Histogram of final positions at y.
axs[1,1].hist(endp_y, bins=30)
axs[1,1].set_title(f"Histograma de posições finais em y. {s} passos - {r} runs")
axs[1,1].set_xlabel("Posição final em Y")
axs[1,1].set_ylabel("Frequência")
axs[1,1].grid()

plt.show()