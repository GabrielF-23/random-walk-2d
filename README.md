# Gerador de Caminhante Aleatório Gaussiano 2D
Gaussian Random Walk 2D Generator

🇧🇷 [Português](#português) | 🇺🇸 [English](#english)

# Português

## Sobre

Esse programa foi desenvolvido como exercício de aprendizado durante minha Iniciação Científica.

O objetivo desse programa foi compreender os conceitos fundamentais de processos estocásticos, difusão, simulações computacionais e modelagem matemática através de um modelo de caminhante aleatório gaussiano em duas dimensões utilizando Python.

## Descrição do modelo

Um caminhante inicia sua trajetória na origem do plano cartesiano,

```
(x, y) = (0,0)
```

A cada passo, um novo deslocamento é gerado em coordenadas polares.

O ângulo é sorteado a partir de uma distribuição uniforme

```
θ ~ U(0,2π)
```

enquanto o módulo do deslocamento é obtido por uma distribuição normal

```
ρ ~ N(0,σ)
```

No código, esses valores são gerados por

```python
theta = np.random.uniform(0, 2*np.pi)
rho = np.random.normal(0, sigma)
```

As coordenadas do caminhante são então atualizadas por

```python
x += rho*np.cos(theta)
y += rho*np.sin(theta)
```

Como o ângulo é uniformemente distribuído, não existe direção preferencial para o movimento. Já o parâmetro σ controla a intensidade das flutuações de cada passo.

Valores maiores de σ produzem trajetórias mais espalhadas, enquanto valores menores resultam em movimentos mais suaves.

## Parâmetros do modelo

O modelo possui três parâmetros principais:

- `n_steps`: número de passos de cada caminhante;
- `n_runs`: número total de caminhantes simulados;
- `sigma`: desvio padrão da distribuição normal utilizada para gerar o comprimento de cada passo.

Por padrão o programa utiliza

```
n_steps = 500
n_runs = 1000
sigma = 1
```

## Gráficos

Após executar o programa, são gerados três gráficos.

### Gráfico A — Trajetória de um caminhante

Mostra o caminho percorrido por um único caminhante no plano XY, indicando a posição inicial e a posição final.

### Gráfico B — Posições finais

Apresenta um gráfico de dispersão contendo as posições finais de todos os caminhantes após o término da simulação.

### Gráfico C — Deslocamento Quadrático Médio (MSD)

Mostra o deslocamento quadrático médio

```
⟨r²(t)⟩
```

calculado ao longo da simulação.

O gráfico também apresenta a curva teórica utilizada para comparação

```
⟨r²(t)⟩ = σ² t
```

permitindo comparar os resultados numéricos com o comportamento esperado do processo difusivo.

## Ferramentas e Bibliotecas

- Python
- NumPy
- Matplotlib

## Licença

Este projeto está licenciado sob a licença MIT.

## Autor

Gabriel Freitas.

# English

WIP.
