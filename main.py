"""
Módulo principal para execução do programa do labirinto.

Este módulo implementa a interface gráfica e controle principal do programa de resolução de labirinto utilizando diferentes algoritmos de busca.

Módulo contém:
    - Configuração do labirinto
    - Inicialização do Pygame
    - Interface para seleção de algoritmos
"""
import pygame # type: ignore
import Busca_Largura
import Busca_Profundidade
from labirinto import Labirinto
from desenhar_Labirinto import desenhar
import sys
import hill_climbing

pygame.init()

def labirinto(): 
    """
    Cria e retorna a matriz que representa o labirinto.

    Esta função:
    1. Define a estrutura do labirinto usando uma matriz 2D
    2. Usa 0 para representar paredes
    3. Usa 1 para representar caminhos livres
    4. Mantém o formato 12x12 do labirinto

    Estrutura do labirinto:
        - 0: representa parede/obstáculo
        - 1: representa caminho livre
        - Dimensões: 12x12 células
        - Entrada: posição [4,11]
        - Saída: posição [10,0]

    Returns:
        List[List[int]]: Matriz 2D representando o labirinto
    """
    labirinto_grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0], 
            [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1],
            [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    return labirinto_grid

labirint = labirinto() 

def executar_largura(labirinto): 
    """
    Executa o algoritmo de Busca em Largura no labirinto.

    Esta função:
    1. Inicia a resolução do labirinto
    2. Executa o algoritmo de Busca em Largura
    3. Mostra o caminho encontrado e número de passos
    4. Desenha o resultado no labirinto

    Args:
        labirinto (List[List[int]]): Matriz 2D representando o labirinto

    Returns:
        None

    Exemplo:
        executar_largura(labirinto_grid)
    """
    print("Iniciando a resolução do labirinto...\n")

    #1. Busca em Largura
    print("Executando Busca em Largura (BFS)...")
    busca_largura = Busca_Largura.resolver(labirinto, [4,11],[10,0])
    print("Caminho encontrado (BFS):", busca_largura)
    print(f"passos: {len(busca_largura)-1}")

    desenhar(labirinto, [4,11],[10,0], busca_largura) 
    print("Resolução completa!")

def executar_profundidade(labirinto):
    """
    Executa o algoritmo de Busca em Profundidade no labirinto.

    Esta função:
    1. Inicia a resolução do labirinto
    2. Executa o algoritmo de Busca em Profundidade
    3. Mostra o caminho encontrado e número de passos
    4. Desenha o resultado no labirinto

    Args:
        labirinto (List[List[int]]): Matriz 2D representando o labirinto

    Returns:
        None

    Exemplo:
        executar_profundidade(labirinto_grid)
    """
    print("Iniciando a resolução do labirinto...\n")

    # 2. Busca em Profundidade
    print("\nExecutando Busca em Profundidade (DFS)...")
    busca_profundidade = Busca_Profundidade.resolver(labirinto, [4,11],[10,0]) 
    print("Caminho encontrado (DFS):", busca_profundidade)
    print(f"passos: {len(busca_profundidade)-1}")

    desenhar(labirinto, [4,11],[10,0], busca_profundidade) 
    print("Resolução completa!")

def executar_hill_climbing(labirinto):
    """
    Executa o algoritmo Hill Climbing no labirinto.

    Esta função:
    1. Inicia a resolução do labirinto
    2. Executa o algoritmo Hill Climbing
    3. Mostra o caminho encontrado e número de passos
    4. Desenha o resultado no labirinto

    Args:
        labirinto (List[List[int]]): Matriz 2D representando o labirinto

    Returns:
        None

    Exemplo:
        executar_hill_climbing(labirinto_grid)
    """
    print("Iniciando a resolução do labirinto...\n")   

    # 3. Heuristica Hill Climbing
    print("\nExecutando Hill Climbing...")
    caminho = hill_climbing.resolver(labirinto, [4, 11], [10, 0])
    print("Caminho encontrado (Hill Climbing):", caminho)
    print(f"passos: {len(caminho)-1}")

    desenhar(labirinto, [4,11],[10,0], caminho)
    print("Resolução completa!")


rodando = True
desenhar(labirint, [4,11],[10,0], None) 
"""
    Função principal que controla o loop do programa e eventos.

    Esta função:
    1. Inicializa o labirinto
    2. Mantém o loop principal do programa
    3. Gerencia eventos do Pygame
    4. Controla o encerramento do programa

    Returns:
        None
    """
while rodando:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    executar_largura(labirint) 
                if event.key == pygame.K_2:
                    executar_profundidade(labirint)
                if event.key == pygame.K_3:
                    executar_hill_climbing(labirint)
                if event.key == pygame.K_d:
                    desenhar(labirint, [4,11],[10,0], None)




