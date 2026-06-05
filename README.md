# Gerador de Caminhante Aleatório 2D
Random Walk 2D Generator

🇧🇷 [Português](#português) | 🇺🇸 [English](#english)
# Português
## Sobre
Esse programa foi desenvolvido como exercicio de aprendizado durante minha Iniciação Cientifica.

O objetivo desse programa foi compreender os conceitos fundamentais de processos estocasticos, simulações computacionais e modelagem matematica atraves de um modelo simples de caminhante aleatorio em duas dimensões em Python.

## Descrição do modelo
Um caminhante começa de um ponto x = 0 (origem).
A cada passo ele tem 25% de chance de escolher dar um passo para direita, esquerda, cima ou baixo.<br>
Cada passo novo é dado por:

        step = random.choice([1,2,3,4])

        if step == 1:
            x += 1
        elif step == 2:
            x -= 1
        elif step == 3:
            y += 1
        else:
            y -= 1
            
Quando `step == 1`: ele soma 1 a posição x dele.<br>
Quando `step == 2`: ele subtrai 1 da posição x dele.<br>
Quando `step == 3`: ele soma 1 a posição y dele.<br>
Quando `step == 4`: ele subtrai 1 da posição y dele.<br>

Cada passo tem a mesma probabilidade de acontecer.<br>

### Parametros do modelo
Temos 2 parametros nesse modelo:<br>
- `r`: número de caminhantes.<br>
- `s`: número de passos.<br>

Altere como desejar, por padrão o modelo vem:<br>
`r = 1000`<br>
`s = 1000`

### Gráficos
Após escolher a quantidade de caminhantes e a quantidade de passos, execute o programa e 
ele vai gerar quatro gráficos:<br>

#### Gráfico A: Trajetória dos caminhantes
Mostra a trajetória de todos os caminhantes em um gráfico X x Y.

#### Gráfico B: Disperção das posições finais
Mostra a disperção das posições finais de cada caminhante.

#### Gráfico C: Histograma das posições finais em X
Mostra a distruibuição das posições finais de cada caminhante no eixo X.

#### Gráfico D: Histograma das posições finais em Y
Mostra a distruibuição das posições finais de cada caminhante no eixo Y.

## Ferramentas e Bibliotecas
- Python
- Matplotlib
- Random
- Numpy

## Licença
Este projeto está licenciado sob a licença MIT.

## Autor
Gabriel Freitas.

# English
WIP.







 
