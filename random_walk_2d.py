import matplotlib.pyplot as plt
import numpy as np


def random_walk2d(n_steps, sigma):
    x = 0
    y = 0

    trajectory_x = [0]
    trajectory_y = [0]

    for i in range(n_steps):

        theta = np.random.uniform(0, 2*np.pi)
        rho = np.random.normal(0, sigma)

        x += rho*np.cos(theta)
        y += rho*np.sin(theta)

        trajectory_x.append(x)
        trajectory_y.append(y)



    return trajectory_x, trajectory_y


n_steps = 500

n_runs = 1000

sigma = 1


walks = []


for i in range(n_runs):
    walks.append(random_walk2d(n_steps, sigma))

fig, axs = plt.subplots(1,3, figsize=(12,4), dpi=120)


x, y = walks[0]

axs[0].plot(x, y, linewidth=1)
axs[0].scatter(0, 0, color="green", s=40, label="Início")
axs[0].scatter(x[-1], y[-1], color="red", s=40, label="Fim")

axs[0].set_title("Trajetória de um Caminhante")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Y")
axs[0].grid()
axs[0].axis("equal")
axs[0].legend()


endp_x = []
endp_y = []


for x, y in walks:
    endp_x.append(x[-1])
    endp_y.append(y[-1])


axs[1].scatter(endp_x, endp_y, s=10)

axs[1].set_title("Posições Finais")
axs[1].set_xlabel("X")
axs[1].set_ylabel("Y")
axs[1].grid()
axs[1].axis("equal")


msd = []


for t in range(n_steps + 1):

    r2 = []

    for x, y in walks:
        r2.append(x[t]**2 + y[t]**2)

    msd.append(np.mean(r2))


axs[2].plot(range(n_steps+1),msd,label="Simulação")


axs[2].plot(
    range(n_steps+1),
    sigma**2*np.arange(n_steps+1),
    label="DQM"
)


axs[2].set_title("Deslocamento Quadrático Médio")
axs[2].set_xlabel("Passos")
axs[2].set_ylabel("<r²>")
axs[2].grid()
axs[2].legend()


fig.suptitle(
    f"Caminhante Aleatório 2D\n"
    f"ρ ~ N(0,{sigma}) e θ ~ U(0,2π) | "
    f"{n_steps} passos - {n_runs} simulações",
    fontsize=14
)


plt.tight_layout()
plt.show()
