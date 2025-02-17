
"""
Módulo para visualização gráfica do labirinto usando Pygame.

Este módulo:
1. Configura a janela de visualização
2. Define constantes de tamanho e cores
3. Implementa a função de desenho do labirinto

Constantes:
    tamanho_celula (int): Tamanho em pixels de cada célula do labirinto
    largura_janela (int): Largura total da janela em pixels
    altura_janela (int): Altura total da janela em pixels
"""
import pygame # type: ignore
tamanho_celula = 55

largura_janela = 12 * tamanho_celula
altura_janela = 12 * tamanho_celula

janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Projeto 1 - Busca")

def desenhar(labirinto, inicio, objetivo, caminho):
    """
    Desenha o labirinto, pontos de início/objetivo e caminho encontrado.

    Esta função:
    1. Itera sobre cada célula do labirinto
    2. Atribui cores diferentes para cada tipo de célula
    3. Desenha retângulos coloridos para representar o labirinto
    4. Adiciona bordas para melhor visualização
    5. Atualiza a tela do Pygame

    Args:
        labirinto (List[List[int]]): Matriz 2D representando o labirinto onde:
            - 0 representa parede/obstáculo
            - 1 representa caminho livre
        inicio (tuple): Coordenadas (x,y) do ponto inicial
        objetivo (tuple): Coordenadas (x,y) do ponto objetivo
        caminho (List[tuple]): Lista de coordenadas representando o caminho encontrado

    Cores utilizadas:
        - Roxo claro (216,191,216): paredes
        - Branco (255,255,255): caminhos livres
        - Preto (0,0,0): bordas das células

    Returns:
        None: Atualiza a visualização na janela do Pygame
    """
    for y, linha in enumerate(labirinto):
        for x, celula in enumerate(linha):
            if celula == 0:  # Parede
                cor = (216, 191, 216)  
            elif celula == 1: 
                cor = (255, 255, 255)
            elif (y, x) == inicio:
                cor = (255, 0, 0)  
            elif (y, x) == objetivo:
                cor = (0, 255, 0)  
            else:
                cor = (255, 255, 255)

            pygame.draw.rect(janela, cor, (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula))

            pygame.draw.rect(
                janela, 
                (0, 0, 0),  
                (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula),
                width=1  
            )

    pygame.display.flip()

    if caminho is not None:
        for i, posicao in enumerate(caminho):
            y, x = posicao
            cor = (255, int(150 * i / len(caminho)), 255 - int(30 * i / len(caminho)))
            pygame.draw.rect(janela, cor, (x * tamanho_celula, y * tamanho_celula, tamanho_celula, tamanho_celula))
            pygame.display.flip()
            pygame.time.delay(100)  