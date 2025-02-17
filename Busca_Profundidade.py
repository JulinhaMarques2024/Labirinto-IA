def resolver(labirinto, inicio, objetivo):
    """
    Implementa o algoritmo de Busca em Profundidade (DFS) para encontrar um caminho no labirinto.

    Esta função:
    1. Utiliza uma pilha para armazenar os caminhos a serem explorados
    2. Explora o labirinto até encontrar becos sem saída
    3. Faz backtracking quando necessário
    4. Verifica vizinhos em 4 direções (cima, direita, esquerda, baixo)
    5. Mantém registro de células visitadas

    Args:
        labirinto (List[List[int]]): Matriz 2D representando o labirinto onde:
            - 0 representa parede/obstáculo
            - 1 representa caminho livre
        inicio (List[int]): Coordenadas [x,y] do ponto inicial
        objetivo (List[int]): Coordenadas [x,y] do ponto objetivo

    Returns:
        List[List[int]]: Lista de coordenadas representando o caminho encontrado,
                        incluindo todos os pontos visitados até encontrar o objetivo.
                        Retorna None se não encontrar caminho válido.
    """
    pilha = [list(inicio)]
    visitados = []

    while pilha:
        atual = pilha.pop()  # Usar pop() para remover o último elemento da pilha
        if list(atual) == list(objetivo):
            visitados.append(atual)
            return visitados

        if atual not in visitados:
            visitados.append(atual)
            vizinhos = [(atual[0] - 1, atual[1]),  # cima
                        (atual[0], atual[1] + 1),  # direita
                        (atual[0], atual[1] - 1),  # esquerda
                        (atual[0] + 1, atual[1])]  # baixo

            for vizinho in vizinhos:
                if vizinho[0] >= 0 and vizinho[0] < len(labirinto) and vizinho[1] >= 0 and vizinho[1] < len(labirinto[0]):
                    if vizinho not in pilha and vizinho not in visitados and labirinto[vizinho[0]][vizinho[1]] == 1:
                        pilha.append(vizinho)  
                        print(pilha)