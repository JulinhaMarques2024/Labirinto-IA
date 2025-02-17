def resolver(labirinto, inicio, objetivo):
    """
    Implementa o algoritmo de Busca em Largura (BFS) para encontrar um caminho no labirinto.

    Esta função:
    1. Explora o labirinto nivel por nivel
    2. Mantém uma pilha de posições a serem visitadas
    3. Rastreia posições já visitadas
    4. Verifica vizinhos válidos em todas as direções
    5. Retorna o caminho quando encontra o objetivo

    Args:
        labirinto (List[List[int]]): Matriz 2D representando o labirinto onde:
            - 0 representa parede/obstáculo
            - 1 representa caminho livre
        inicio (List[int]): Coordenadas [x,y] do ponto inicial
        objetivo (List[int]): Coordenadas [x,y] do ponto objetivo

    Returns:
        List[List[int]]: Lista de coordenadas representando o caminho encontrado,
                        incluindo todos os pontos visitados até encontrar o objetivo.
                        Retorna lista de visitados se não encontrar caminho.
    """
    pilha = [list(inicio)]
    visitados = []

    while pilha:
        atual = pilha.pop(0)
        print(list(atual))
        print(list(objetivo))
        if list(atual) == list(objetivo):
            visitados.append(atual)
            return visitados

        if atual not in visitados:
            visitados.append(atual)
            vizinhos = [(atual[0] + 1, atual[1]), (atual[0] - 1, atual[1]), (atual[0], atual[1] + 1), (atual[0], atual[1] - 1)]

            for vizinho in vizinhos:
                if vizinho[0] >= 0 and vizinho[0] < len(labirinto) and vizinho[1] >= 0 and vizinho[1] < len(labirinto[0]):
                    if vizinho not in pilha and vizinho not in visitados and labirinto[vizinho[0]][vizinho[1]] == 1:
                        pilha.append(vizinho) 
    return visitados