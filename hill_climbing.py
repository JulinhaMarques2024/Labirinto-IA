def resolver(labirinto, inicio, objetivo):
    """
    Implementa o algoritmo Hill Climbing para encontrar um caminho no labirinto.

    Esta função:
    1. Converte as coordenadas de entrada para tuplas
    2. Utiliza uma função interna para gerar vizinhos válidos
    3. Mantém uma fila de estados e caminhos
    4. Rastreia posições visitadas usando um conjunto
    5. Explora vizinhos não visitados em busca do objetivo

    Args:
        labirinto (List[List[int]]): Matriz 2D representando o labirinto onde:
            - 0 representa parede/obstáculo
            - 1 representa caminho livre
        inicio (List[int]): Coordenadas [x,y] do ponto inicial
        objetivo (List[int]): Coordenadas [x,y] do ponto objetivo

    Returns:
        List[tuple]: Lista de tuplas (x,y) representando o caminho encontrado do
                    início até o objetivo. Retorna None se não encontrar caminho.
    """
    inicio = tuple(inicio)
    objetivo = tuple(objetivo)

    def gerar_vizinhos(atual, visitados, labirinto):
        vizinhos = [(atual[0] - 1, atual[1]),  # cima
                    (atual[0], atual[1] + 1),  # direita
                    (atual[0], atual[1] - 1),  # esquerda
                    (atual[0] + 1, atual[1])]  # baixo

        vizinhos_validos = []
        for x, y in vizinhos:
            if (0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]) and labirinto[x][y] == 1 and (x, y) not in visitados):
                vizinhos_validos.append((x, y))
        return vizinhos_validos

    fila = [(inicio, [inicio])]  
    visitados = set()  
    while fila:
        estado_atual, caminho = fila.pop(0)

        if estado_atual == objetivo:
            return caminho

        visitados.add(estado_atual)

        for vizinho in gerar_vizinhos(estado_atual, visitados, labirinto):
            if vizinho not in visitados:
                fila.append((vizinho, caminho + [vizinho]))

    return None